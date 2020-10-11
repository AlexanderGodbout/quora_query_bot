


def create_questions_table():
    query = ''' 
    CREATE TABLE IF NOT EXISTS Questions ( 
        Q_id INT AUTO_INCREMENT PRIMARY KEY 
        ,text VARCHAR(255)
        ,is_grammatical BIT
        ,is_unique BIT
        ,is_viral BIT
        ,is_obsessional BIT
        ,is_accepted BIT
        ,source VARCHAR(255) 
        ,earnings DECIMAL(13, 2)
        ,views 
        ,ad_impressions INT
        ,answers INT
        ,external_traffic DECIMAL(5, 3)
        ,internal_traffic DECIMAL(5, 3)
        ,create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ,update_date DATE
        ,build DECIMAL(4, 2)
    )
    '''





def insert_into_table(): 
    query = '''
    INSERT INTO Questions(
        text, is_grammatical, is_unique, is_viral, is_obsessional, is_accepted, source, earnings, views, ad_impressions, answers, external_traffic, internal_traffic, create_date, update_date, build) 
        VALUES ('To do or not to do?', 1, 1, 1, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1)
    '''