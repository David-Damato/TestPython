from dataclasses import dataclass, field

from typing import List

from worker import Worker


class Room:

    workers: List[Worker]

    max_places: int

    def __init__(self, max_places=5):

        self.max_places = max_places

        self.workers = []

    def add_worker(self, worker: Worker):

        if len(self.workers) >= self.max_places:

            print("not enough place !")

            return

        if worker in self.workers:

            print("You're already there")

            return

        self.workers += [worker]
