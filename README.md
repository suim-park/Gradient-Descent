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
    ![Plot_1000_0 1](https://github.com/suim-park/Gradient-Descent/assets/143478016/ea158283-bcdc-4f52-a625-7d856d4e833c)
</br>

* __`Case 2`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 1000  # SET THIS
      learning_rate = 0.5  # SET THIS
      ```
  - Result Plot
    ![Plot_1000_0 5](https://github.com/suim-park/Gradient-Descent/assets/143478016/3643229a-0744-43a5-82d1-9fe99f1ec38e)
</br>

* __`Case 3`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 1000  # SET THIS
      learning_rate = 0.01  # SET THIS
      ```
  - Result Plot
    ![Plot_1000_0 01](https://github.com/suim-park/Gradient-Descent/assets/143478016/2237bdec-9d17-4a56-a27a-be057a822312)
</br>

* __`Case 4`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 500  # SET THIS
      learning_rate = 0.5  # SET THIS
      ```
  - Result Plot
    ![Plot_500_0 5](https://github.com/suim-park/Gradient-Descent/assets/143478016/4f022724-ed26-4038-b2ac-d01c3f40d4ae)
</br>

* __`Case 5`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 500  # SET THIS
      learning_rate = 0.1  # SET THIS
      ```
  - Result Plot
    ![Plot_500_0 1](https://github.com/suim-park/Gradient-Descent/assets/143478016/e9960da7-832d-4263-95f9-d4286d0edc0d)
</br>

* __`Case 6`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 500  # SET THIS
      learning_rate = 0.01  # SET THIS
      ```
  - Result Plot
    ![Plot_500_0 01](https://github.com/suim-park/Gradient-Descent/assets/143478016/c6f3512e-0e34-4d91-ad9c-4026fe527a93)
</br>

* __`Case 7`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 100  # SET THIS
      learning_rate = 0.5  # SET THIS
      ```
  - Result Plot
    ![Plot_100_0 5](https://github.com/suim-park/Gradient-Descent/assets/143478016/3a388bf4-fc77-4c39-a1e7-4267f21364b6)
</br>

* __`Case 8`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 100  # SET THIS
      learning_rate = 0.1  # SET THIS
      ```
    - Result Plot
    ![Plot_100_0 1](https://github.com/suim-park/Gradient-Descent/assets/143478016/ee44c744-ab2b-4256-aa17-257d23b0806a)
</br>

* __`Case 9`__ _(Recommended)_
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 100  # SET THIS
      learning_rate = 0.01  # SET THIS
      ```
  - Result Plot
    ![Plot_100_0 01](https://github.com/suim-park/Gradient-Descent/assets/143478016/ddc89c30-e2e7-460e-954b-5078a56fce81)

</br>
