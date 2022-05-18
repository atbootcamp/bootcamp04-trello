from main.trello.api.rest_base_manager import RESTBaseManager

class LabelsManager(RESTBaseManager):
    """Class which can be used to manage Trello Boards through the API"""

    def __init__(self, method=None):
        """ Construct the necessary attributes for the BoardsManager
        :param method: obj  RequestManager object which is used to handle the API requests
        """
        super().__init__(method)

    def create_label(self, name, color, **kwargs):               
        endpoint = 'boards/QI9piQFl/labels?'
        payload = {
            "name": name,
            "color": color,
        }
        # join dicts, add/replace the 'fields' query param if it was passed
        if kwargs:
            payload = {**kwargs, **payload}
        status_code, response = self.method.post_request(endpoint, payload=payload)
        return status_code, response

    def get_labels(self,**kwargs):
        endpoint = 'boards/QI9piQFl/labels?'
        status_code, response = self.method.get_request(endpoint, **kwargs)
        return status_code, response

    def get_label(self, id):
        endpoint= f'labels/{id}?'
        status_code, response = self.method.get_request(endpoint)
        return status_code, response

    def create_label_card(self, card_id, name, color, **kwargs):
        endpoint=f'cards/{card_id}/labels?'
        payload = {
            "name": name,
            "color": color,
        }
        # join dicts, add/replace the 'fields' query param if it was passed
        if kwargs:
            payload = {**kwargs, **payload}
        status_code, response = self.method.post_request(endpoint, payload=payload)
        return status_code, response
        
    def update_label(self, label_id, name, color, **kwargs):
        endpoint=f'labels/{label_id}?'
        payload = {
            "name": name,
            "color": color,
        }
        # join dicts, add/replace the 'fields' query param if it was passed
        if kwargs:
            payload = {**kwargs, **payload}
        status_code, response = self.method.put_request(endpoint, payload=payload)
        return status_code, response

    def delete_label_board(self, id_label):
        endpoint = f"labels/{id_label}?"
        return self.method.delete_request(endpoint)

    def delete_label_card(self, id_card,id_label):
        endpoint = f'cards/{id_card}/idLabels/{id_label}?'
        return self.method.delete_request(endpoint)
        








a=LabelsManager()
status_code, response = a.delete_label_card('628264cf49d65c88ae11443d','62850da3acbdbe54297cf023')
print(response)





