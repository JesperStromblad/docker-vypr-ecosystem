original_pwd=`pwd`

if ! command -v virtualenv &> /dev/null
then
  echo "Please install virtualenv.  You can normally do this with pip."
  exit
fi

# setup global virtual environment
# the requirements of each repository cloned will be added
virtualenv --python=python2.7 venv
source venv/bin/activate

# clone and setup visualisation tool
# cd = /
git clone https://github.com/pyvypr/VyPR-visualisation.git
cd VyPR-visualisation
pip install -r requirements.txt

# clone and setup test project
# cd = /VyPR-visualisation/
cd test-project
pip install -r requirements.txt
git clone https://github.com/pyvypr/VyPRLocal-py2.git VyPR

# cd into test-project, run instrumentation then run the program under monitoring
python VyPR/instrument.py
python main.py

cd ..

# cd to VyPR-visualisation/src
cd src/

# setup visualisation tool launch alias
python launch.py --port 9001 --instrumentation-stream http://localhost:9003/event_stream/instrumentation/ --monitoring-stream http://localhost:9003/event_stream/monitoring/ &  

