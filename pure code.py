from surprise import SVD
from surprise import Dataset
from surprise import Reader

# Load the data
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df, reader)

# Use the SVD algorithm
algo = SVD()

# Train the model
train_set = data.build_full_trainset()
algo.fit(train_set)

# Make predictions
predictions = algo.predict(uid, iid)
