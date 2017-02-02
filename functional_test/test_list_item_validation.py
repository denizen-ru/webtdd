from functional_test.base import FuncionalTest


class ItemValidationTest(FuncionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with sametext for the item, which now works

        # Perversely, she now decides to submit a second blank list item

        # She receives a similar warrning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
