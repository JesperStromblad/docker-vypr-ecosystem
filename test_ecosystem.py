import docker
import unittest


class testVyPREcoSystem(unittest.TestCase):



  def test_containers(self):

    """
    Tests containers where they are running properly. We need to ensure that we are testing the correct containers for the ecosystem
    """


    containers_to_test = ['vyprjupyter:latest', 'verdict:latest', 'vypr:latest', 'ci:latest']

    test_counter = 0

    client = docker.from_env()

    for container in client.containers.list():

      if container.image.tags[0] in containers_to_test:

          if container.status == 'running':

              test_counter = test_counter + 1

    self.assertEquals(test_counter,3)






  def test_vypr_visualization(self):


      """
      Test VyPR Visualization tool. We pass two important event streams and check whether they return a valid response
      """

      client = docker.from_env()

      for container in client.containers.list():

        if container.image.tags[0] == 'verdict:latest':

          log = container.logs()

          self.assertTrue(log.__contains__('HTTP/1.1'))


      url_instr = 'http://localhost:9003/event_stream/instrumentation/'
      url_monitor = 'http://localhost:9003/event_stream/monitoring/'

      import requests,json
      resp = requests.get(url_instr)
      self.assertIsNotNone(json.dumps(resp.content))


      resp = requests.get(url_monitor)
      self.assertIsNotNone(json.dumps(resp.content))



  def test_vypr_analysis_enviroment(self):

      """
	  Test VyPR Analysis tool. We check the url which handles fetching the code.
	  """


      url_to_test = 'http://localhost:9002//get_source_code/2/'

      import requests

      resp = requests.get(url_to_test)

      self.assertEquals(resp.status_code,200)

  def test_vypr_gitlab_ci(self):

        """
        Test VyPR in CI process. We check that a valid verdict database is generated after CI pipeline is completed
        """

        import time
        time.sleep(200)     # Wait for CI to get completed. TODO we need to find another way
        import requests
        resp = requests.get('https://gitlab.com/package4conf/sample-perfci/-/jobs/artifacts/master/raw/perfdata/verdicts.db?job=performance_testing')
        self.assertEquals(resp.status_code,200)


  def test_vypr_jupyter(self):

      """
	  Test VyPR Jupyter notebook. We only check whether the notebook is running properly. TODO: This will require some mechanism to check the process in notebook
	  """


      client = docker.from_env()

      for container in client.containers.list():

          if container.image.tags[0] == 'vyprjupyter:latest':

              log = container.logs()

              start = log.index('http')

              url_with_characters = log[start:440]

              end_of_url = url_with_characters.index('[')

              get_token = url_with_characters[:end_of_url]

              start_token = get_token.index('?')

              token = get_token[start_token:]

              url = "http://127.0.0.1:9005/"+token

              import urllib2

              response = urllib2.urlopen(url)

              resp_code = response.code

              self.assertEquals(resp_code, 200)


if __name__ == '__main__':

    unittest.main(verbosity=2)
