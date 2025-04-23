import firebase_admin
from google.cloud.exceptions import NotFound
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

matches_ref = db.collection("hello")

# Lấy tất cả documents trong collection "matches"
def get_list_documents():
    docs = matches_ref.stream()

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

# Tạo mới trận đấu
def create_new_match():
    doc_ref = matches_ref.add({
        'player1': 'Nam',
        'player2': 'Linh',
        'score1': 2,
        'score2': 3,
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    # print("Added match with ID:", doc_ref[1].id)

# Xóa trận đấu
def remove_match():
    matches_ref.document("63qaRNCOypPlLMxwjF8G").delete()

# Cập nhật trận đấu cụ thể
def update_match():
    try:
        matches_ref.document("63qaRNCOypPlLMxwjF8G").update({
            'score1': 4
        })
    except NotFound:
        print("Lỗi Không tìm được document")    

# Cập nhật toàn bộ thông tin của trận đấu
def update_full_match():
    matches_ref.document("63qaRNCOypPlLMxwjF8G").set({
        'player1': 'Tùng',
        'player2': 'An',
        'score1': 1,
        'score2': 1
    })

update_full_match()
# Theo dõi danh sách trận đấu -> Cái này đẩy qua client thôi, nhưng làm sao để giấu api key thì chưa biết