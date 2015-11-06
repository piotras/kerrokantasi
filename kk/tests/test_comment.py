from kk.tests.base import BaseKKDBTest


class TestComment(BaseKKDBTest):

    def setup(self):
        super(TestComment, self).setup()

        self.default_content = 'I agree with you sir Lancelot. My favourite colour is blue'
        self.comment_data = {
            'content': self.default_content,
        }

    def test_55_add_comment_without_authentication(self, default_hearing):
        # post data to hearing ednpoint /v1/hearings/<hearingID>/comments/
        response = self.client.post(self.get_hearing_detail_url(default_hearing.id, 'comments'), data=self.comment_data)
        assert response.status_code == 403

    def test_55_add_comment_to_hearing_empty_data(self, default_hearing):
        # authenticate first
        self.user_login()

        # post data to hearing ednpoint /v1/hearings/<hearingID>/comments/
        response = self.client.post(self.get_hearing_detail_url(default_hearing.id, 'comments'), data=None)
        assert response.status_code == 400

        data = self.get_data_from_response(response)
        assert data is not None

    def test_55_add_comment_to_hearing_invalid_data(self, default_hearing):
        # authenticate first
        self.user_login()

        # post data to hearing ednpoint /v1/hearings/<hearingID>/comments/
        invalid_data = {
            'invalidKey': 'Korben Dallas multipass'
        }
        response = self.client.post(self.get_hearing_detail_url(default_hearing.id, 'comments'), data=invalid_data)
        assert response.status_code == 400

        data = self.get_data_from_response(response)
        assert data is not None

    def test_55_add_comment_to_hearing(self, default_hearing):
        # authenticate first
        self.user_login()

        # post data to hearing ednpoint /v1/hearings/<hearingID>/comments/
        response = self.client.post(self.get_hearing_detail_url(default_hearing.id, 'comments'), data=self.comment_data)
        assert response.status_code in [200, 201]

        data = self.get_data_from_response(response)
        assert data['created_by'] == self.username
        assert data['content'] == self.default_content
        assert data['votes'] == 0
