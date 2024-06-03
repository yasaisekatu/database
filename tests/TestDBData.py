#!/usr/bin/env python3

# ユニットテスト用ライブラリ
import unittest
import os
# DB操作用にmysql-connector-pythonをインポート
import mysql.connector

# 環境変数 MYSQL_USER の値を DBUSER 変数に代入
DBUSER = os.getenv('MYSQL_USER')
# 同様にMYSQL_PASSWORDとMYSQL_DATABASEを取得
DBPASS = os.getenv('MYSQL_PASSWORD')
DBHOST = "db"
DBNAME = os.getenv('MYSQL_DATABASE')

# unittest.TestCaseを継承したクラスを作成、クラス名はTestDBAccess
class TestDBData(unittest.TestCase):
    # テストケース実行前に呼ばれるメソッド
    def setUp(self):
        # DBに接続
        self.conn = mysql.connector.connect(
            user=DBUSER,
            password=DBPASS,
            host=DBHOST,
            database=DBNAME
        )
        # カーソルを取得
        self.cur = self.conn.cursor()

    def tearDown(self) -> None:
        self.conn.close()

    # personテーブルの内容の確認
    def test_check_person_data(self):
        """personテーブルのレコードについて以下の検証を行う
        * レコード件数が6件以上あること
        * レコードの中でnameが「糸井五郎」のレコードがあること
        """
        self.cur.execute("SELECT * FROM person")
        rows = self.cur.fetchall()
        self.assertGreaterEqual(len(rows), 6)
        # nameが「糸井五郎」のレコードがあるか
        names = [row[1] for row in rows]
        self.assertIn('糸井五郎', names)

    # companyテーブルの内容を確認
    def test_check_company_data(self):
        """companyテーブルのレコードについて以下の検証を行う
        * 3件以上レコードがあること
        * nameが「神戸工業」のレコードがあること
        """
        self.cur.execute("SELECT * FROM company")
        rows = self.cur.fetchall()
        self.assertGreaterEqual(len(rows), 3)
        # nameが「神戸工業」のレコードがあるか
        names = [row[1] for row in rows]
        self.assertIn('神戸工業', names)

if __name__ == '__main__':
    unittest.main()
