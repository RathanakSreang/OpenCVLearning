import numpy as np

class Searcher:
    def __init__(self, index):
        self.index = index

    def search(self, queryFeatures):
        # init result
        results = {}

        #loop all over index
        for (k, features) in self.index.items():
            # compute the chi-squared betweeen the feature
            # in index and queryFeature use chi-square distance which is normally
            # use in computer vision for histogram comparing
            d = self.chi2_distance(features, queryFeatures)

            # update the result directory
            results[k] = d

        # let's sort our result
        results = sorted([(v, k) for (k, v) in results.items()])

        return results

    def chi2_distance(self, histA, histB, eps = 1e-10):
        d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
                        for (a, b) in zip(histA, histB)])
        return d


