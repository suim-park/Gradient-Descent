# Homework #2 :pencil:
## Information :computer:
* `Subject`: __Introduction to Natural Language Processing__
* `Professor`: __Patrick Wang__
* `Assignment`: __HW #2 Gradient Descent__
* `Name`: __Suim Park (sp699)__

## Notification :heavy_check_mark:
* __`OS Module`__ </br>
  Whenever running the code, I consistently received a warning message about `multiple copies of the OpenMP runtime`. To avoid this and execute the code, I included __'OS'__ module within the code.
  ```Python
  import os
  os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
  ```


* __`matplotlib`__ </br>
  To make some line plots and bar plots, I imported __'matplotlib'__ library, especially as __'matplotlib.pyplot'__.
  ```Python
  import matplotlib.pyplot as plt
  ```

## Test case :pushpin:

* __`Case 1`__ _(Recommended)_
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 1000  # SET THIS
      learning_rate = 0.1  # SET THIS
      ```
  - Result Plot
    ![Plot_1000_0 1](https://github.com/suim-park/Gradient-Descent/assets/143478016/99b15b49-96b5-4a25-bf68-ef5f2ce4c10a)
</br>

* __`Case 2`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 1000  # SET THIS
      learning_rate = 0.5  # SET THIS
      ```
  - Result Plot
    ![Plot_1000_0 5](https://github.com/suim-park/Gradient-Descent/assets/143478016/fa931585-f0ae-4647-8558-65ef10453c76)
</br>

* __`Case 3`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 1000  # SET THIS
      learning_rate = 0.01  # SET THIS
      ```
  - Result Plot
    ![Plot_1000_0 01](https://github.com/suim-park/Gradient-Descent/assets/143478016/cee29ddd-06ca-4d13-96d6-5bdca4c33223)
</br>

* __`Case 4`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 500  # SET THIS
      learning_rate = 0.5  # SET THIS
      ```
  - Result Plot
    ![Plot_500_0 5](https://github.com/suim-park/Gradient-Descent/assets/143478016/ab0b7ed2-b32e-49e1-976c-aa998e9ab71b)
</br>

* __`Case 5`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 500  # SET THIS
      learning_rate = 0.1  # SET THIS
      ```
  - Result Plot
    ![Plot_500_0 1](https://github.com/suim-park/Gradient-Descent/assets/143478016/5d283f67-1c80-4837-91ca-32ef314046da)
</br>

* __`Case 6`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 500  # SET THIS
      learning_rate = 0.01  # SET THIS
      ```
  - Result Plot
    ![Plot_500_0 01](https://github.com/suim-park/Gradient-Descent/assets/143478016/561c51d6-2442-47af-aa98-dba805e51d3b)
</br>

* __`Case 7`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 100  # SET THIS
      learning_rate = 0.5  # SET THIS
      ```
  - Result Plot
    ![Plot_100_0 5](https://github.com/suim-park/Gradient-Descent/assets/143478016/b5eceba5-0b6f-4da6-adef-ec8ecf756caa)
</br>

* __`Case 8`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 100  # SET THIS
      learning_rate = 0.1  # SET THIS
      ```
    - Result Plot
    ![Plot_100_0 1](https://github.com/suim-park/Gradient-Descent/assets/143478016/49356493-c4f9-4fa7-af24-6d2c255c8cfa)
</br>

* __`Case 9`__ _(Recommended)_
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 100  # SET THIS
      learning_rate = 0.01  # SET THIS
      ```
  - Result Plot
    ![Plot_100_0 01](https://github.com/suim-park/Gradient-Descent/assets/143478016/d90d5ed9-e576-44a3-9c07-4211974b758d)
</br>


