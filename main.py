import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json


class FirestoreClient():
    def __init__(self):
        self.config = {
                  "type": "service_account",
                  "project_id": "",
                  "private_key_id": "",
                  "private_key": "",
                  "client_email": "",
                  "client_id": "",
                  "auth_uri": "",
                  "token_uri": "",
                  "auth_provider": "",
                  "client_x509_cert_url": "",
                  "universe_domain": "googleapis.com"
                }
        self.db_client = self.get_client(self.config)




    @staticmethod
    def get_client(config):
        cred = credentials.Certificate(config)
        firebase_admin.initialize_app(cred, {'projectID': 'program-c37c4'})
        return firestore.client()


    def get_doc(self, collection_id, doc_id):
        return self.db_client.collection(collection_id).document(doc_id).get().to_dict()

    def set_doc(self, collection_id, doc_id, data):
        return self.db_client.collection(collection_id).document(doc_id).set(data)



firestore_client = FirestoreClient()

if __name__ == '__main__':
    document = firestore_client.get_doc('cafe', 'users')
    # document = firestore_client.get_doc('cafe', 'menu')
    # document = firestore_client.get_doc('cafe', 'messages')
    # document = firestore_client.get_doc('cafe', 'admin')
    print(document)
