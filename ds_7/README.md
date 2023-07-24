# Hometask 7
This week, we learned how recommender systems work. We suggest that you get acquainted with the [surprise](https://surpriselib.com/) library, which is essentially an add-on to the familiar scikit-learn library for training recommender system models.

Take the [movielens](https://surprise.readthedocs.io/en/stable/dataset.html) dataset and build a matrix factorization model. In this library, it is called SVD. Select the best parameters using cross-validation, also experiment with other calculation [algorithms](https://surprise.readthedocs.io/en/stable/prediction_algorithms_package.html) (SVD++, NMF) and choose the one that will be optimal.

You can find tips on how to build this model in the documentation for this library.

## Additional task with an asterisk
For a deeper dive into the algorithm, we suggest implementing the collaborative filtering algorithm from scratch. To do this, we can use our homework from module 3. If we modify the loss function and the calculation of gradients, we can build a matrix factorization algorithm.

[Here](https://colab.research.google.com/drive/1biZdo4pc_Kkm-JvZsuadqDVphfUu1sGk?usp=sharing) you can see the formulas and download the dataset. And here are links to [movie titles](https://drive.google.com/file/d/12XeO4KXQfbvvTdLFbkYA-BeXzhlNnnuo/view?usp=sharing) and [ratings](https://drive.google.com/file/d/17V9OhXeZH9Wv17Nkh-Tqxa8svEmRZcIp/view?usp=sharing).