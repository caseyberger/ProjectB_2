# -*- coding: utf-8 -*-
"""monteCarloPi

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vAnMSWBx2UMEDjV8Wi6_YOhEJcuxES4F
"""

#monteCarlopPi.py
# import sys, random, and pandas modules

#class begins: MonteCarloPi()

    '''
      A class to store

      Attributes:
        radius (int): the radius of the square the
        length (int): size of the square the darts are thrown in
        num_it (int): number of iterations
        num_darts (int): number of dart throws, randomly selected from range (100, 10000)

    '''

    # constructor w params, self, radius, num_it



        # assigns num_darts as a randome int between 100 and 10000

    # method throw_dart

        '''
          throw_dart is a method for Class MonteCarloPi

          returns boolean for if the throw landed inside the circle

        '''
        # get a float between 1.0 and 10.0

        # if float is > 1.0 and < 7.85, dart landed inside the circle
        
        # else circle = False
    
    # method many_throws()

        '''
          many_throws is a method for Class MonteCarloPi

          it creates dataframe for the Object

        '''
        # create empty throws_list

        # for all num_darts append result of throw_dart() to list

        # create a dataframe from throws_list

        # return dataframe

  # method summarize_results()

        '''
          summarize_results is a method for Class MonteCarloPi

          returns number of hits inside and outside the circle in hit_results_df

        '''
        # return value_counts() of column in df

  # method calc_pi() 
  # w param hit_results_df

      '''
        calc_pi is a method for Class MonteCarloPi

        it calculates pi based on the area of a circle and the area of a square:
          pi = 4*hit_results_df[0]/(hit_results_df[0] + hit_results_df[1])

      '''
      # return pi