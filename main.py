import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json


class FirestoreClient():
    def __init__(self):
        self.config = {
                  "type": "service_account",
                  "project_id": "program-c37c4",
                  "private_key_id": "b0beed2d8f190fccfe669de0f6b6eb6b12b9d1fd",
                  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC6cOFTlqo8vyYG\nnDdRLcLP/lDPj9OV2p3Pk5C8mgwcTXkkLnnoDpLcUF6r1N0wXdmBbj+j030itne0\nSzEjde0ZVrzIy19Gn6eacwTcUHsEk1QKx8yinCN7xjYx4AR42hr5qIolBKnx9DB/\nNdnhSLfp84d0KpHLkYGBbJ8Bd+01SnEc0A/ljZe114dJYatVV2idVI5+gWQiiXJJ\nVxhlvNlnv/aGDdOrO8b9G7j/ROYMLIeP6HbGULmTsSq7YqexCwbIGyHdwTDOqLzW\nN9c8N8wrZZOJrXVduzqqH7PD4x2J6zXft26g7rfQn3NgFj5tnChrLoyiUMM9qDHB\nviGC8gC9AgMBAAECggEAAMlkypRS6+0yssVe56tklXCYK1d4oR9skPl7m1QfylCj\nzS72BV4LO4au3LmuiRuIRT4UGZhVCZdslasQjjG2zIL3JeQupuo+ebJmMQenMTuk\noL9yJn9cYWXJdtOgRKIirqWAzktlbAnntA22Jy6YehJG9RP95/+rpMJprqI5vAvu\nU2vuOuSuX9YekOL/3LJEjVGcGPHjL+M0fkehL36L3FaJo/scVz1UkoSKWog36556\nnceLN3GTp/AT4bW6noIj6s8LmgRNxCVMcaWsgQYyywNVTQO0nmUtaghzr9HVaERN\nVtP63kKtrA5s57fgPcwEpAhQ+cfJzqx8GGSa0/DYwQKBgQD7084CGU0QwjwLbAXr\nETecMf5t3wgnNUU6LysNOM4ThNSvU9pn6Zrc17pzij6FvMd+OOLIfC5GKL7AAer8\nmLsMjaj3wrHbC79lyTSeQUH7PTSY7Afqk05nPCLsoekg0J8wZWpHrvIYnRzt6eh4\nA+JikMXAtkjSl5GUL42E1LNlQQKBgQC9h7iMdOKMW4cCdHU1wL9TIicGfIICcysz\nyP1s01FurSerW22cKmjIsg3XqCNqaYpxelEIdiqO2IepPkZVJSowshlxTAvdsYbl\nsq1RyrvLxn/F4/bAbGMEf1Y0rj19AtTmT9oL6MkTCCyg5wYrwO9Kv8SaPUBtl7NP\n9IegHCWQfQKBgC8l0pYWApW2p+NDkEAYcx7tRUNw1Gfy00k3d4n8Lqj8340L2AJI\nfFQIl8H2Cgqj832wTNVYWpmMG1p7gXFVbv/ErfPlIcNvCaCW8SEH+sB9DxHqbvj+\nJ1mwqqE/FxSruoInGqTdHjp5f+cTOhDuOT5W+I9CEZRMCFeEJ6zM3eGBAoGACzWP\nsJ7pFywCnB6PIBK6PgxzCmsqtUJid7mXY2xMEKOlCPlrTiUj9VqyfuKu1YhQa820\nJS/37GLaAyRvvHFqQV8HKjA5M29gbw1WOtQmrzKaM/X7jf3bDVUKoCr97/rO5KAs\nYS/vVHTTTuDa+JN8k4sr8YNV4CVssXng25NOlXECgYBbF5tfROF9gBV7A3eplkM5\n6XBqFcrIQSPpP1kQAnTnjk/710W37J8VHQIS7yOooEHZigvugIAx0M93DSbQDXOU\nEYy0bwAGJhskSIwdJ38CNQH3MCNMGDUDPmetyzuLLFQhfwFYwTpvjclyhgBQ+P1D\nITbsbLeU2s02pFQ+B67ZQg==\n-----END PRIVATE KEY-----\n",
                  "client_email": "firebase-adminsdk-6fark@program-c37c4.iam.gserviceaccount.com",
                  "client_id": "116318153712826133104",
                  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                  "token_uri": "https://oauth2.googleapis.com/token",
                  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6fark%40program-c37c4.iam.gserviceaccount.com",
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