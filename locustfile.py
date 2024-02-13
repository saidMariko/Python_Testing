from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(1, 2.5)

    @task
    def load_main_page(self):
        response = self.client.get("/")
        assert response.elapsed.total_seconds() < 5.0, "La page d'accueil prend plus de 5 secondes à charger"

    @task
    def load_points_display(self):
        response = self.client.get("/pointsDisplay")
        assert response.elapsed.total_seconds() < 5.0, "La page des points du club prend plus de 5 secondes à charger"

    @task
    def load_archive(self):
        response = self.client.get("/archive")
        assert response.elapsed.total_seconds() < 5.0, "La page d'archive prend plus de 5 secondes à charger"

    @task
    def update_club(self):
        response = self.client.post("/purchasePlaces", data={
            'competition': 'CAN',
            'club': 'Simply Lift',
            'places': 18
        })
        assert response.elapsed.total_seconds() < 2.0, "La mise à jour du club prend plus de 2 secondes"

    @task
    def load_showSummary(self):
        response = self.client.post("/showSummary", data={
            'email': 'john@simplylift.co'
        })
        assert response.elapsed.total_seconds() < 5.0, "La page de résumé prend plus de 5 secondes à charger"

    @task
    def load_book(self):
        response = self.client.get("/book/CAN/Simply Lift")
        assert response.elapsed.total_seconds() < 5.0, "La page de réservation prend plus de 5 secondes à charger"