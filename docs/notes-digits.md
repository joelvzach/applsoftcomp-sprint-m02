I used a combination of the scikit learn TSNE documentation to create my parameters, a scikit learn example project that used TSNE in part of it for a similar ML digits vizualization to know how to input the data and use the generated transform in a plot. I also used Chat GPT to understand how the data is being stored and how I should extract it for the purpose of using in a t-SNE transform.

AI and the example projects had many paramters when creating the t-SNE function, but I chose to only use a few as the default values in the scikit documentation seemed reasonable.

I used a block gradient for my coloring rather than a continuous gradient as the clusters are representing integer steps rather than continuous values.


https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
https://scikit-learn.org/stable/auto_examples/manifold/plot_lle_digits.html