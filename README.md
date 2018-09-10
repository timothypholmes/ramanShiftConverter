# Raman Shift Converter

## ramanConvert.py

### Steps to run the ramanConvert.py in a CLI UNIX enviorment 

1. Make it executable.
  > chmod a+x ramanConvert.py
  
2. Run.
  > ./ramanConvert.py
  
  
## ramanConvertCLI.py

### Steps to run the ramanConvert.py in a CLI UNIX enviorment 

1. Make it executable.

  > chmod a+x ramanConvertCLI.py
  
2. To convert between wavelength and wave number run:

  > python -c 'from ramanConvertCLI import convertLenToNum; print convertLenToNum()'
  
3. To convert between wave number and wavelength run:

  > python -c 'from ramanConvertCLI import convertNumToLen; print convertNumToLen()'
