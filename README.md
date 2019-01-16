# Splitwise Python Application

This is a Python application to split expenses, provided the participating members and payments done by them. 

Steps to use the app:
(You may create a Python virtual env in and use the app inside the virtual env.)

1. Switch directory to base folder SplitwiseApp. 

2. Set env var PYTHONPATH to the application folder Splitwise.
```
export PYTHONPATH=`pwd`
```

3. To run the application, 
```
python src/main.py --input_file sample_inputs/sample_input.txt
```

4. To run tests, 
```
python tests/splitwise_test.py
```
