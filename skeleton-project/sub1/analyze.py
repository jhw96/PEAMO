from numpy import fabs
from pandas.core import groupby
from parse import load_dataframes
import pandas as pd
import shutil
import numpy as np


def sort_stores_by_score(dataframes, n=20, min_reviews=30):
    """
    Req. 1-2-1 각 음식점의 평균 평점을 계산하여 높은 평점의 음식점 순으로 `n`개의 음식점을 정렬하여 리턴합니다
    Req. 1-2-2 리뷰 개수가 `min_reviews` 미만인 음식점은 제외합니다.
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )  # left_on 왼쪽 data 에서 id를 기준으로, right_on 오른쪽 data 에서 store를 기준으로 값이 같은 애들(공통되는 부분)을 merge
    scores_group = stores_reviews.groupby(
        ["store", "store_name"])  # 가게 id로 그룹을 묶고 그 안에서 다시 가게 이름으로 그룹화 한다

    scores_group = scores_group.filter(lambda s: len(s) >= min_reviews).groupby(
        ["store", "store_name"])  # 리뷰 수가 최소 리뷰수 이상인 애들만 다시 그룹화한다

    # 그룹화된 애들 중 Integer 값들을 평균 낸다
    scores = scores_group.mean()
    # 평균 낸 애들을 score 를 기준으로 내림차순 정렬
    scores = scores.sort_values(by="score", ascending=False)
    return scores.head(n=n).reset_index()


def get_most_reviewed_stores(dataframes, n=20):
    """
    Req. 1-2-3 가장 많은 리뷰를 받은 `n`개의 음식점을 정렬하여 리턴합니다
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )  # left_on 왼쪽 data 에서 id를 기준으로, right_on 오른쪽 data 에서 store를 기준으로 값이 같은 애들(공통되는 부분)을 merge
    scores_group = stores_reviews.groupby(
        ["store", "store_name"])  # 가게 id로 그룹을 묶고 그 안에서 다시 가게 이름으로 그룹화 한다

    scores = scores_group.count()  # 해당 가게가 받은 리뷰 개수 파악
    scores = scores.sort_values(
        by="score", ascending=False)  # 리뷰 수에 따라 내림차순 정리

    return scores.head(n=n).reset_index()


def get_most_active_users(dataframes, n=20):
    """
    Req. 1-2-4 가장 많은 리뷰를 작성한 `n`명의 유저를 정렬하여 리턴합니다.
    """
    # 유저 id로 그룹화 한 뒤에 유저가 남긴 리뷰의 개수에 따라 내림차순 정렬
    reviews_group = dataframes['reviews'].groupby(
        "user").count().sort_values(by="score", ascending=False)

    return reviews_group.head(n=n).reset_index()


def get_user_store(dataframes):
    """
    Req. 1-4-1 유저 - 음식점 행렬 생성
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )  # left_on 왼쪽 data 에서 id를 기준으로, right_on 오른쪽 data 에서 store를 기준으로 값이 같은 애들(공통되는 부분)을 merge

    # user id 값을 모두 가져와서 중복되는 값을 제거
    user_list = list(set(stores_reviews['user'].values.tolist()))
    user_list.sort()  # user id 를 오름차순으로 정렬
    # store name 을 모두 가져와서 중복되는 값을 제거
    store_list = list(set(stores_reviews['store_name'].values.tolist()))

    # 유저 id 값을 행으로 가게 이름을 열로 만들고 값은 모두 0으로 된 dataframe 생성
    df = pd.DataFrame(data=np.nan, index=user_list, columns=store_list)

    user_group = stores_reviews.sort_values(
        by='user').groupby(['user', 'store_name']).mean().loc[:, 'score']  # 유저 id 와 가게이름으로 group 한 후 평균을 내고 그 중 score 값만 남긴다

    for index, score in user_group.items():  # index 에는 (user_id, score_name) 이 score 에는 평점이 있다
        user, store_name = index
        # df 에서 행에서는 유저 id 를 열에서는 가게 이름을 찾아 값을 평점으로 변경
        df.loc[user, store_name] = score

    return df.astype(pd.SparseDtype("float"))


def main():
    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    stores_most_scored = sort_stores_by_score(data)

    print("[최고 평점 음식점]")
    print(f"{separater}\n")
    for i, store in stores_most_scored.iterrows():
        print(
            "{rank}위: {store}({score}점)".format(
                rank=i + 1, store=store.store_name, score=store.score
            )
        )
    print(f"\n{separater}\n\n")

    stores_most_review = get_most_reviewed_stores(data)

    print("[리뷰 개수 기준 음식점 정렬]")
    print(f"{separater}\n")
    for i, store in stores_most_review.iterrows():
        print(
            "{rank}위: {store}(리뷰 {score}개)".format(
                rank=i + 1, store=store.store_name, score=store.score
            )
        )
    print(f"\n{separater}\n\n")

    users_most_review = get_most_active_users(data)

    print("[리뷰 개수 기준 유저 정렬]")
    print(f"{separater}\n")
    for i, store in users_most_review.iterrows():
        print(
            "{rank}위: {user}(리뷰 {score}개)".format(
                rank=i + 1, user=store.user, score=store.score
            )
        )
    print(f"\n{separater}\n\n")

    user_store_arr = get_user_store(data)

    print("[유저 - 음식점 행렬]")
    print(f"{separater}\n")
    print(user_store_arr)
    print(f"\n{separater}\n\n")


if __name__ == "__main__":
    main()
