import unittest
from bookdetails_server import BookDetails
import bookdetails_pb2

class TestBookDetailsServer(unittest.TestCase):
    def test_grpc_server_book_details(self):
        service = BookDetails()
        bdresponse = service.GetBookDetails(bookdetails_pb2.BookDetailsRequest(author='Kurt Vonnegut'), None)
        bd_arr = []
        for bdr in bdresponse.bookDetails:
            bd_arr.append([bdr.author, bdr.title, bdr.quotes])
        vonnegut_row = ['Kurt Vonnegut', 'Slaughterhouse-Five', '“So it goes.”']
        self.assertIn(vonnegut_row, bd_arr)

    def test_grpc_server_author_list(self):
        service = BookDetails()
        aaresponse = service.GetAuthorsList(bookdetails_pb2.AuthorsListRequest(), None)
        auth_arr = []
        for aar in aaresponse.authorsList:
            auth_arr.append([aar.author])
        self.assertIn(['Jane Austen'], auth_arr)

if __name__ == '__main__':
    unittest.main()
