
from recommender.movie_recommender import MovieRecommender

def main():

    recommender = MovieRecommender("data/movies.csv")

    print("\nMOVIE RECOMMENDATION SYSTEM")
    print("---------------------------")

    print("\nRecommendations for Genre='Action', Language='Tamil':")

    recommendations = recommender.recommend(
        genre='Action',
        language='Tamil'
    )

    print(recommendations.to_string(index=False))

if __name__ == "__main__":
    main()
