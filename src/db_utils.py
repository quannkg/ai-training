import pandas as pd
import mysql.connector
from config import DB_CONFIG

def load_vietlott_mega_645_data():
    conn = mysql.connector.connect(**DB_CONFIG)
    query = """
        SELECT ky_quay, ngay_mo_thuong, day_so_trung_thuong
        FROM lotte_result
        WHERE loai_ve_so = 'MEGA_6_45'
        ORDER BY ngay_mo_thuong ASC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def load_vietlott_power_655_data():
    conn = mysql.connector.connect(**DB_CONFIG)
    query = """
        SELECT ky_quay, ngay_mo_thuong, day_so_trung_thuong
        FROM lotte_result
        WHERE loai_ve_so = 'POWER_6_55'
        ORDER BY ngay_mo_thuong ASC
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


