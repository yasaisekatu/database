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
class TestDBStructure(unittest.TestCase):
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

    # テーブル構造の確認(person)
    def test_table_check_person(self):
        """テーブルpersonの構造が正しいこと
        テーブルpersonは以下のレコードを持つ
        * uid: int型、主キー、auto_increment
        * name: varchar(20)
        * company_id: int
        * age: int
        """
        self.cur.execute("DESCRIBE person")
        desc = self.cur.fetchall()
        self.assertEqual(('uid', 'int', 'NO', 'PRI', None, 'auto_increment'), desc[0])
        self.assertEqual(('name', 'varchar(20)', 'NO', '', None, ''), desc[1])
        self.assertEqual(('company_id', 'int', 'NO', '', None, ''), desc[2])
        self.assertEqual(('age', 'int', 'NO', '', None, ''), desc[3])

    # テーブル構造の確認(company)
    def test_table_check_company(self):
        """テーブルpersonの構造が正しいこと
        テーブルpersonは以下のレコードを持つ、全てNULLは許容されない
        * cid: int型、主キー、auto_increment
        * name: varchar(20)
        * address: varchar(40)
        """
        self.cur.execute("DESCRIBE company")
        desc = self.cur.fetchall()
        self.assertEqual(('cid', 'int', 'NO', 'PRI', None, 'auto_increment'), desc[0])
        self.assertEqual(('name', 'varchar(20)', 'NO', '', None, ''), desc[1])
        self.assertEqual(('address', 'varchar(40)', 'NO', '', None, ''), desc[2])




if __name__ == '__main__':
    unittest.main()
