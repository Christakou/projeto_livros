import pandas as pd
from main.models import Book, Influencer
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    def handle(self, *args, **options):
        df = pd.read_csv('main/management/commands/all_celebrities_data_processed.csv')
        df = df[~pd.isna(df['ISBN'])]
        for book_title in df['title'].unique():
            print(f'Adding {book_title} to the DB')
            filtered = df[df['title']==book_title].head(1)
            for index, row in filtered.iterrows():
                newbook = Book(title_en=row['title'],author=row['author'],isbn=row['ISBN'])
                newbook.save()

        for celeb in df['influencer'].unique():
            print(f'Adding {celeb} to the DB')
            influencer = Influencer(name=celeb)
            influencer.save()
            filtered = df[df['influencer']==celeb]
            for index, row in filtered.iterrows():
                
                try:
                    print(f'Added book {row["title"]} to recommended by {celeb}')
                    book_to_add = Book.objects.get(isbn=row['ISBN'])
                    influencer.recommended_books.add(book_to_add)
                except Exception as e:
                    print(f'An exception occured when trying to add books for {celeb},\
                        trying to add row: {row} \n got the following exception: {str(e)}')
                    





