import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'governance.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def get_article(article_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        res = dict(row)
        res['topics'] = json.loads(res['topics'])
        return res
    return None

def get_framework(framework_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM frameworks WHERE id = ?', (framework_id,))
    row = cursor.fetchone()
    if not row:
        conn.close()
        return None
    
    fw = dict(row)
    fw['key_provisions'] = json.loads(fw['key_provisions'])
    fw['risk_classification'] = json.loads(fw['risk_classification'])
    
    cursor.execute('SELECT * FROM mappings WHERE framework_id = ?', (framework_id,))
    mappings = {}
    for mrow in cursor.fetchall():
        mappings[mrow['provision']] = {
            'csoai_articles': json.loads(mrow['csoai_articles']),
            'alignment': mrow['alignment'],
            'mechanism': mrow['mechanism']
        }
    fw['csoai_mappings'] = mappings
    conn.close()
    return fw

def list_frameworks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM frameworks')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def get_universal_principles():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM universal_principles')
    rows = cursor.fetchall()
    conn.close()
    res = {}
    for row in rows:
        res[row['name']] = {
            'csoai_articles': json.loads(row['csoai_articles']),
            'coverage': row['coverage'],
            'description': row['description']
        }
    return res

def get_alignment_matrix():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM alignment_matrix')
    rows = cursor.fetchall()
    conn.close()
    res = {}
    for row in rows:
        if row['part'] not in res:
            res[row['part']] = {}
        res[row['part']][row['framework']] = row['level']
    return res

def get_topic_keywords():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT value FROM settings WHERE key = ?', ('topic_keywords',))
    row = cursor.fetchone()
    conn.close()
    if row:
        return json.loads(row['value'])
    return {}

def search_articles_by_topic(keyword):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM articles WHERE topics LIKE ?', (f'%"{keyword}"%',))
    rows = cursor.fetchall()
    conn.close()
    res = []
    for row in rows:
        d = dict(row)
        d['topics'] = json.loads(d['topics'])
        res.append(d)
    return res

def resolve_framework_key(name):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Simple lookup for now
    cursor.execute('SELECT id FROM frameworks WHERE name = ? OR id = ?', (name, name))
    row = cursor.fetchone()
    if not row:
        # Try some common aliases
        aliases = {
            'NIST': 'nist_ai_rmf',
            'ISO': 'iso_42001',
            'OECD': 'oecd_principles',
            'UNESCO': 'unesco_ethics',
            'EU': 'eu_ai_act'
        }
        res = aliases.get(name.upper())
        conn.close()
        return res
    
    res = row['id']
    conn.close()
    return res
