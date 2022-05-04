class Merger:
    def __init__(self, cbf_percentage, cf_percentage, user_percentage):
        self.cbf_percentage = cbf_percentage
        self.cf_percentage = cf_percentage
        self.user_percentage = user_percentage

    @staticmethod
    def find(ranks, ranking):
        index = -1
        for item in ranks:
            index += 1
            if item[0] == ranking[0] and item[1] == ranking[1] and item[2] == ranking[2]:
                return index
        return -1

    def format(self, ranking):
        ranking = ranking[0:3]
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

    def merge(self, cbf_ranking, cf_ranking, user_preference):
        final_ranking = []

        user_preference[3] = user_preference[3] * self.user_percentage / 100

        for rank in cf_ranking:
            if rank[0] == user_preference[0] and rank[1] == user_preference[1] and rank[2] == user_preference[2]:
                user_preference[3] += rank[3] * self.cf_percentage / 100
            else:
                rank[3] = rank[3] * self.cf_percentage / 100
                final_ranking.append(rank)

        # Values in cbf_ranking are not necessarily unique
        # Compulsory courses can be similar to the same set of elective courses
        for rank in cbf_ranking:
            if rank[0] == user_preference[0] and rank[1] == user_preference[1] and rank[2] == user_preference[2]:
                user_preference[3] += rank[3] * self.cbf_percentage / 100
            else:
                found_idx = self.find(final_ranking, rank)
                if found_idx != -1:
                    final_ranking[found_idx][3] += rank[3] * self.cbf_percentage / 100
                else:
                    rank[3] = rank[3] * self.cbf_percentage / 100
                    final_ranking.append(rank)

        final_ranking.append(user_preference)
        final_ranking.sort(key=lambda x: x[3], reverse=True)
        return self.format(final_ranking)
