from typing import final
from matplotlib.style import use


class Merger:
    def __init__(self, cbf_percentage, cf_percentage, user_percentage, user_rank):
        self.cbf_percentage = cbf_percentage
        self.cf_percentage = cf_percentage
        self.user_percentage = user_percentage
        self.user_rank = user_rank

    def format(self, ranking):
        result = []
        for rank in ranking:
            string_format=""
            for i in range(len(rank)-1):
                if i == len(rank)-2:
                    string_format += rank[i]
                else:
                    string_format += rank[i]+", "
            result.append(string_format)
        return result

    @staticmethod
    def find(ranking, combination):
        index = -1
        for item in ranking:
            index += 1
            if item[0] == combination[0] and item[1] == combination[1] and item[2] == combination[2]:
                return index
        return -1

    def merge_ranking(self, final_ranking, method_ranking, percentage):
        for combination in method_ranking:
            # Multiply with the set percentage
            combination[3] = combination[3] * percentage / 100
            # Use a helper function which returns the index of the combination in the ranking in case it is found, or -1 otherwise
            index = self.find(final_ranking, combination)
            # If the combination has not been processed before, then add to the final ranking
            if index == -1:
                final_ranking.append(combination)
            # Otherwise, add the duplicate's weight to the combination in the final ranking
            else:
                final_ranking[index][3] += combination[3]
        return final_ranking

    def merge(self, cbf_ranking, cf_ranking, user_preference):
        final_ranking = []
        # Assign a rank to the user's combination and multiply it by the set percentage
        user_preference.append(self.user_rank * self.user_percentage / 100)
        # Add the user's preference
        final_ranking.append(user_preference)
        # Add the Content-Based Filtering results
        final_ranking = self.merge_ranking(final_ranking, cbf_ranking, self.cbf_percentage)
        # Add the Collaborative Filtering results
        final_ranking = self.merge_ranking(final_ranking, cf_ranking, self.cf_percentage)
        final_ranking.sort(key=lambda x: x[3], reverse=True)
        return final_ranking


