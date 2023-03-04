#!/usr/bin/python3
"""
100-main
"""

def main():
    count_words = __import__('100-count').count_words
    result = count_words('hello', ['REDDIT', 'german', 'HI', 'whynot'])
    print('OK')

if __name__ == '__main__':
    main()
