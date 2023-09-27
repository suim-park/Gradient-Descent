# Homework #2 :pencil:
## Information :computer:
* `Subject`: __Introduction to Natural Language Processing__
* `Professor`: __Patrick Wang__
* `Assignment`: __HW #2 Gradient Descent__
* `Name`: __Suim Park (sp699)__

## Notification :heavy_check_mark:
* Whenever I ran the code, I consistently received a warning message about `multiple copies of the OpenMP runtime`. To avoid this and execute the code, I included
  ```Python
  import os
  os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
  ```
  within the code.

## Test case :pushpin:

* __`Case 1`__ _(Recommended)_
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 1000  # SET THIS
      learning_rate = 0.1  # SET THIS
      ```
  - Result Plot
    ![Plot_1000_0 1](https://github.com/suim-park/Markov-Text-Generator/assets/143478016/f76124ec-6507-495f-93b5-cfb8b10f441a)
</br>

* __`Case 2`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 100  # SET THIS
      learning_rate = 0.5  # SET THIS
      ```
  - Result Plot
    ![Plot_100_0 5](https://github.com/suim-park/Markov-Text-Generator/assets/143478016/a1986122-c8bf-424b-a81a-286f61278ecb)
</br>

* __`Case 3`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 100  # SET THIS
      learning_rate = 0.1  # SET THIS
      ```
  - Result Plot
    ![Plot_100_0 1](https://github.com/suim-park/Markov-Text-Generator/assets/143478016/4c2df906-db6d-4aa3-ad3f-b4315ce31d06)
</br>

* __`Case 4`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 500  # SET THIS
      learning_rate = 0.5  # SET THIS
      ```
  - Result Plot
    ![Plot_500_0 1](https://github.com/suim-park/Markov-Text-Generator/assets/143478016/ea19c87e-28ad-4aad-aa32-55ffd86db5ad)
</br>

* __`Case 5`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 500  # SET THIS
      learning_rate = 0.1  # SET THIS
      ```
  - Result Plot
    ![Plot_500_0 1](https://github.com/suim-park/Markov-Text-Generator/assets/143478016/bb42d88f-3480-4e5c-a75e-dbabcd1a9284)
</br>

* __`Case 6`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 1000  # SET THIS
      learning_rate = 0.5  # SET THIS
      ```
  - Result Plot
    ![Plot_1000_0 5](https://github.com/suim-park/Markov-Text-Generator/assets/143478016/4f846c9e-eff7-4b1b-9261-1e34adbb6b95)
</br>

* __`Case 7`__
    - Test
      ```Python
      # set number of iterations and learning rate
      num_iterations = 1000  # SET THIS
      learning_rate = 0.01  # SET THIS
      ```
  - Result Plot
    ![Plot_1000_0 01](https://github.com/suim-park/Markov-Text-Generator/assets/143478016/a15a1b87-7ec3-474b-8658-04a0fcabecc0)

