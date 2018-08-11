import proto_small_pb2
import proto_avg_pb2
import proto_big_pb2
import random
import string


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def create_small_message():
    tweet = proto_small_pb2.Tweet()
    tweet.user_id = generate_random_string(32)
    tweet.first_name = generate_random_string(random.randint(3, 10))
    tweet.last_name = generate_random_string(random.randint(5, 12))
    tweet.user_type = proto_small_pb2.Tweet.REGULAR
    tweet.tweet_chars.extend(list(generate_random_string(random.randint(20, 100))))
    # if this was complex type you would use aa= tweet_chars.add() and edit aa

    tweet2 = {"user_id": tweet.user_id, "first_name": tweet.first_name, "last_name": tweet.last_name,
              "user_type": "REGULAR", "tweet_chars":tweet.tweet_chars[:]}
    return tweet, tweet2


def create_avg_message():
    meme = proto_avg_pb2.MemeImage()
    meme.user.user_id = generate_random_string(32)
    meme.user.first_name = generate_random_string(random.randint(3, 10))
    meme.user.last_name = generate_random_string(random.randint(5, 12))
    meme.title = generate_random_string(random.randint(50, 150))
    meme.content = bytes(generate_random_string(random.randint(100000, 200000)), 'utf-8')
    meme.top_string = generate_random_string(random.randint(100, 200))
    meme.bottom_string = generate_random_string(random.randint(200, 500))
    meme.likes = 6
    meme.hates = 42

    meme2 = {"user": {"user_id": meme.user.user_id, "first_name": meme.user.first_name,
                      "last_name": meme.user.last_name, "user_type": "FREE"},
             "title": meme.title, "top_string": meme.top_string, "bottom_string": meme.bottom_string,
             "content": meme.content, "likes": 6, "hates": 42}
    return meme, meme2


def create_big_message():
    mod_time = "6/6/6"
    dir_folders = proto_big_pb2.DirFolders()
    folder_dict = {}
    dir_folders.details = generate_random_string(random.randint(50, 150))
    dir_folders.base_folder.path = "/"
    dir_folders.base_folder.last_mod = mod_time
    folder_dict.update({"details": dir_folders.details, "base_folder": {"path":"/", "last_mod": mod_time,
                        "files": [], "folders":[]}})
    for i in range(random.randint(100, 400)):
        dir_file = dir_folders.base_folder.files.add()
        dir_file.file_name = generate_random_string(random.randint(10, 150))
        dir_file.content = bytes(generate_random_string(random.randint(100000, 200000)), 'utf-8')
        dir_file.last_mod = mod_time
        folder_dict["base_folder"]["files"].append({"file_name": dir_file.file_name, "content": dir_file.content, "last_mod": mod_time})
        dir_folder = dir_folders.base_folder.folders.add()
        dir_folder.path = generate_random_string(random.randint(10, 150))
        dir_folder.last_mod = mod_time
        sub_dir_file = dir_folder.files.add()
        sub_dir_file.file_name = generate_random_string(random.randint(10, 150))
        sub_dir_file.content = bytes(generate_random_string(random.randint(100000, 200000)), 'utf-8')
        sub_dir_file.last_mod = mod_time
        folder_dict["base_folder"]["folders"].append({"path": dir_folder.path, "last_mod": mod_time, "files": [{
            "file_name": sub_dir_file.file_name, "content": sub_dir_file.content, "last_mod": mod_time
        }]})

    return dir_folders, folder_dict
