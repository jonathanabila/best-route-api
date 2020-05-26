# Best Route API

## Requirements
 - Docker
 - Docker-Compose
 
### How to run the project
`$ docker-compose up api`

if you want to raise the environment with the interface in the terminal you must do:
`$ docker-compose run terminal`

#### Dependency
You must place the file `input-routes.csv` inside the dist directory for both interfaces.

### How to use the API

#### GET /best_route
Displays the route with the best cost and the path to be taken.

```shell script
curl --location --request GET 'http://localhost:5000/best_route?source=GRU&destination=BRC'
```

```json
{
  "cost": 10,
  "route": "GRU - BRC"
}
```

#### POST /best_route
Register a new route and its cost.

```shell script
curl --location --request POST 'http://localhost:5000/best_route' \
--header 'Content-Type: application/json' \
--data-raw '{
	"source": "SDU",
	"destination": "GRU",
	"cost": 25
}'
```

```json
{
  "route": {
    "cost": 25,
    "destination": "GRU",
    "source": "SDU"
  },
  "status": "added"
}
```

### Monitoring
Integration with new relic for basic request metrics.


### Exceptions
To facilitate error handling, all errors that have some information about the application have their description below 
and which code accompanies it. Thus, messages can be improved or changed, but the code will never be replaced or 
changed if its meaning is not exactly as described.

1. Wrong edges data - The information used to build the graphic contains invalid information.
2. Edge n1 n2 already exists - The edge n1 and n2 is already registered.
3. Such source node doesn't exist - The source node is not registered.
4. Such destination node doesn't exist - The destination node is not registered.
5. Such nodes don't connect -Such nodes don't connect.


### Repository / code organization
A well written code, in my point of view, includes linter tools and for that a pre commit hook has been configured in 
the repository, it contains the following tools that I like: black and flake8. Some more checks are applied, 
but none close to the functioning of the 3 mentioned.


### CI/CD
A basic configuration was applied using travis and code cov to build the tests.
The integration allows a test coverage report along with pull requests, as well as the build guarantee.


### Algorithms considered

1. [Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
2. [A*](https://en.wikipedia.org/wiki/A*_search_algorithm)
3. [Greedy Best-First-Search](https://www.mygreatlearning.com/blog/best-first-search-bfs/)


### Bibliography

##### Introduction to A*
https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
https://www.redblobgames.com/pathfinding/a-star/introduction.html

##### Observations

The topic `## Explicando ##` in the challenge contains an incorrect example, the cheapest route that should be displayed is ** 1 **.

### Special Thanks to: [Maria Boldyreva] (https://dev.to/mxl/dijkstras-algorithm-in-python-algorithms-for-beginners-dkc)
