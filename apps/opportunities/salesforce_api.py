import requests
from apps.opportunities.models import Opportunity

class SalesforseAPI():
    def __init__(self) -> None:
        self.__user = 'maryna@loka.com'
        self.__pass = 'Nfhfrfy77'
        self._auth_token = None

    def _get_access_token(self):
        data = {
            'grant_type': 'password',
            'client_id': '3MVG9t0sl2P.pBypsE7uKNeDz2sRO44kUOa2FoRnuQ.DNfu.H4QUl_NKC6FImDRqEBmi7Z79bDENI7lMpPQzj',
            'client_secret': '588CE933E020409B4664651DAECDBDAE33BBB54E3079F37582EF1983CF87B228',
            'username': self.__user,
            'password': self.__pass
            }
        access_response = requests.post('https://loka4-dev-ed.my.salesforce.com/services/oauth2/token', data).json()
        return access_response['access_token']

    @property
    def auth_token(self):
        if not self._auth_token:
            self._auth_token = self._get_access_token()
        return self._auth_token

    def get_opps(self):
        listviews = requests.get(
            'https://loka4-dev-ed.my.salesforce.com/services/data/v53.0/sobjects/Opportunity/listviews',
            headers={'Authorization': f'Bearer {self.auth_token}'}
            ).json()['listviews']

        # all_opps = list(filter(lambda a: a['label'] == "All Opportunities", listviews))
        all_opps_response = [view for view in listviews if view['label'] == "All Opportunities"]
        all_opps_response = all_opps_response[0]
        all_opps = requests.get(
            f'https://loka4-dev-ed.my.salesforce.com/{all_opps_response["resultsUrl"]}',
            headers={'Authorization': f'Bearer {self.auth_token}'}
            ).json()['records']
        # print(all_opps)
        # print(len(all_opps))

        for record in all_opps:
            for fields in record['columns']:
                if fields['fieldNameOrPath'] == 'Name':
                    name = fields['value']
                    customer = fields['value']
                elif fields['fieldNameOrPath'] == 'Amount':
                    budget = fields['value']
                elif fields['fieldNameOrPath'] == 'StageName':
                    status = fields['value']
            db_upd_table_row = Opportunity.objects.update_or_create(name=name, customer=customer, budget=budget, status=status, is_opportunity=True, is_project=False)
            db_upd_table_row[0].save()
        return all_opps
