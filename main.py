import version

from worker import Worker

from bureau import Room


version.increment_version(3)


gens = []


for i in range(5):

    gens += [Worker("worker"+str(i), 50*i, "dev"+str(i))]


room1 = Room(max_places=2)

room2 = Room()


room1.add_worker(gens[0])

room1.add_worker(gens[1])

room1.add_worker(gens[2])


room2.add_worker(gens[2])

room2.add_worker(gens[2])

room2.add_worker(gens[3])

room2.add_worker(gens[4])

app = Flask(__name__)
