import sys
import datetime


def main():
    post_name = sys.argv[1]
    now = str(datetime.datetime.now())
    date = now.split(' ')[0]
    time = now.split(' ')[1].split('.')[0]
    fout = open('_posts/'+date+'-'+post_name+'.markdown','w')
    fout.write('---\n')
    fout.write('layout: post\n')
    fout.write('title:  \n')
    fout.write('data:   '+date+' '+time+ ' -0500\n')
    fout.write('categories: cove\n')
    fout.write('---\n')
    fout.close()

if __name__ == '__main__':
    main()