'''
Lecture 16: Divide and Conquer -- Fast Fourier Transform (FFT)
Fourier Transform
    F(jw) = integral from -inf to inf f(t)e^(-2jwt)dt
    It decomposes the signal in the time domain into the frequency domain
    The square wave on the top left is composed of a sum of multiple sine waves
    Allows us to visualize a frequency of waves
Discrete Fourier Transform (DFT)
    DFT is a discrete representation of the continuous Fourier transform, which can be fed into a computer
    Let N samples be denoted by r = 0,1,...,N-1
        Ar = sum k to N-1 (Xke^(-2jwkT))
    Ar is the rth coefficient of the DFT
    Xk is the kth sample of the time series
    Using conventional methods, the DFT algorithm takes O(N^2) operations
Fast Fourier Transform (FFT)
    It is a numerically efficient way to calculate the DFT
    It was originally developed by Gauss around 1805, but rediscovered by Cooley and Tukey in 1965
    The FFT algorithm exploits the symmetries of e^(-j*2pi/N*kn)
        Let WN = e^(-j*2pi/N)
    Complex conjugate symmetry
    Periodicity in n,k
Application: Audio Fingerprinting
    Audio fingerprinting is a signature that summarizes an audio recording
    Also known as Content-Based audio Identification (CBID)
    The best known application are apps like Shazam and SoundHound, that link unlabeled audio recordings and find it


'''