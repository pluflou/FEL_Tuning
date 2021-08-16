import numpy as np
from constants import m_e, e, c, hc, I_A, K_u, lambda_u, k_u, L_u, eta, JJ

def resonantLambda(gamma_beam, K_u, lambda_u):
    return lambda_u * (1 + K_u**2 /2) / (2 * gamma_beam**2)

def rhoFEL(current_beam, sigma_beam, gamma_beam):
    rho = 1/4 * (current_beam/I_A/ np.pi**2 * lambda_u**2/gamma_beam**3/sigma_beam**2 * (K_u*JJ)**2)**(1/3)
    return rho

def gainLength1D(rho, lambda_u):
    return 0.045944074618482676 * lambda_u / rho # prefactor is 1./(4.*np.pi*np.sqrt(3))

def getLambdaMX(Lg1D, sizes, lambda_rad, emittance, lambda_u, sig_pz, mean_pz):
    # Ming Xie perturbative fitting formula, effects of energy spread, emittance and diffraction
    eta_d = Lg1D/(2*sizes**2)*lambda_rad/(2*np.pi) # OK
    eta_e = 4*np.pi*Lg1D/lambda_rad *emittance /(sizes**2/emittance) # OK
    eta_g = (4*np.pi/lambda_u)*(sig_pz/mean_pz)*Lg1D  # OK
    
    # coefficients
    a = np.array( [0.45, 0.57, 0.55, 1.6, 3., 2., 0.35, 2.9, 2.4, 51.,\
               0.95, 3., 5.4, 0.7, 1.9, 1140., 2.2, 2.9, 3.2] )
    
    LambdaMX = a[0]*(eta_d**a[1]) + a[2]*(eta_e**a[3]) + a[4]*(eta_g**a[5])\
    + a[6]*(eta_e**a[7])*(eta_g**a[8]) + a[9]*(eta_d**a[10])*(eta_g**a[11]) \
    + a[12]*(eta_d**a[13])*(eta_e**a[14]) + a[15]*(eta_d**a[16])*(eta_e**a[17])*(eta_g**a[18])
    
    return LambdaMX

def gainLength(Lg1D, LambdaMX):
    return Lg1D * (1. + LambdaMX)

def Pbeam(gamma_beam, current_beam):
    # kinetic power of e-beam
    # [A] x unitless x [MV] = [MW]
    return m_e * gamma_beam * current_beam / 10**3 # to GeV

def shot_noise(rho, lambda_rad, beam_current, gamma_beam):
    N = (beam_current*lambda_rad/(c*e))    
    beam_power = Pbeam(gamma_beam, beam_current)
    return 6*np.sqrt(np.pi)*rho**2*beam_power/(N*np.sqrt(np.log(N/rho)))

# def shotNoise(rho, lambda_rad, gamma_beam, z):
#     sig_w = np.sqrt( 3*np.sqrt(3)*rho/k_u/z ) * 2*np.pi*c/lambda_rad
#     return rho*gamma_beam*sig_w/np.sqrt(2*np.pi)
    
def Psat(LambdaMX, rho, P_beam):
    return 1.6/(1+LambdaMX)**2 * rho * P_beam 

def Pz(Pnoise, exp_arg):
    return Pnoise/9 * np.exp(exp_arg)