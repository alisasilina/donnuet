from http.server import SimpleHTTPRequestHandler, HTTPServer, BaseHTTPRequestHandler
import socketserver
from urllib import request, parse

import pymongo
import pprint

client = pymongo.MongoClient('localhost', 27017)
db = client['NUET-questionnaire']
BIGSTR = """
    <div class="teacher unvoted">
          <img src="assets/images/teacher-icon.png" alt="teacher icon" />
          <div class="teacher__name">
            <h3>{name}</h3>
          </div>
          <h5 class="study">{subject}</h5>
          <div class="stars">
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
            <i class="fas fa-star"></i>
          </div>
          <!-- Button trigger votting modal -->
          <button
            type="button"
            class="btn btn-outline-green"
            data-toggle="modal"
            data-target="#modal"
          >
            Голосувати!
          </button>

          <!-- Modal with voting questions -->
          <div
            class="modal fade"
            id="modal"
            tabindex="-1"
            role="dialog"
            aria-labelledby="modalLabel"
            aria-hidden="true"
          >
            <div class="modal-dialog" role="document">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="modalLabel">
                    Голосування
                  </h5>
                  <button
                    type="button"
                    class="close"
                    data-dismiss="modal"
                    aria-label="Close"
                  >
                    <span aria-hidden="true">&times;</span>
                  </button>
                </div>
                <div class="modal-body">
                  <form action="/voting?email={login}" method="POST">
                    <input value='{name}' class='d-none' name='teacher_name'>
                    <ol>
                    <li><b>Викладання матеріалу</b> (ясність, доступність, чіткість; роз'яснює складні питання, виділяє головні моменти)</li>
                    <select id="q1" name='q1' required>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>

                    <li><b>Контакт з аудиторією</b> (вміння вѝкликати і підтрѝмати зацікавленість аудиторії, слідкує за реакцією аудиторії, задає питання, спонукає до дискусії, вміє зняти напруження і втому аудиторії)</li>
                    <select id="q2" name='q2' required>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>

                    <li><b>Оцінювання навчальних досягнень</b> (дотримання заявлених критеріїв оцінювання, прозорість системи накопичення балів, вимогливість і об'єктивність в оцінці студентів)</li>
                    <select id="q3" name='q3' required>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>

                    <li><b>Культура мовлення</b> (рівень володіння мовою, чіткість дикції, темп викладання матеріалу)</li>
                    <select id="q4" name='q4' required>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>

                    <li><b>Стимулювання самостійних навчальних зусиль студентів</b> (надання додаткових інформації, матеріалів, посилань, завдань за предметом для стимулювання і задоволення пізнавальних інтересів студентів)</li>
                    <select id="q5" name='q5' required>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>

                    <li><b>Рівень організованості</b> (умілість та ефективність використання часу занять, дотримання графіку навчального процесу, розкладу занять та консультацій)</li>
                    <select id="q6" name='q6' required>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>

                    <li><b>Педагогічна майстерність</b> (прояв творчого підходу і зацікавленості до дисципліни, яку викладає; використання активних методів проведення занять: дискусії, рольові ігри, індивідуальні та групові презентації тощо)</li>
                    <select id="q7" name='q7' required>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>

                    <li><b>Психологія спілкування</b> (доброзичливість і такт по відношенню до студентів, терпіння, зацікавленість в успіхах студентів)</li>
                    <select id="q8" name='q8' required>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>

                    <li><b>Зворотній зв’язок</b> (аналіз виконаних студентами завдань, відповіді на запитання, надання необхідних пояснень)</li>
                    <select id="q9" name='q9' required>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>

                    <li><b>Володіння сучасними технологіями навчання</b> (вміння використовувати мультимедійні та інтерактивні засоби навчання)</li>
                    <select id="q10" name='q10' required>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                    </select>
                  </ol>
                  </div>
                  <div class="modal-footer">
                    <button
                    type="button"
                    class="btn btn-outline-secondary"
                    data-dismiss="modal"
                    >
                    Скасувати
                  </button>
                  <!-- <button
                  type="button"
                  class="btn btn-green"
                  data-dismiss="modal"
                  aria-label="Close"
                >ОК</button> -->
                  <input type="submit" class="btn btn-green" value='Проголосовать'>
                </div>
              </form>
              </div>
            </div>
          </div>
        </div>
"""

BUTTON = """<button
            type="button"
            class="btn btn-outline-green"
            data-toggle="modal"
            data-target="#modal"
          >
            Проголосувати!
          </button>"""
      
SPAN = """<span>Already voted</span>
              <form action="/" method="GET">
                  <input type="submit" class="btn btn-green" value='Finish'>
              </form>"""

RESULTS_STR = """
<div class='teacher voted'>
            <div class='teacher__info'>
              <img src="assets/images/teacher-icon.png" alt="teacher icon">
              <div class='teacher__name'>
                <h3>{name}</h3>
              </div>
              <p>Середня оцінка:<br><span class='votes__number'>{score}</span></p>
            </div>
            <div class='teacher__details' onClick="detailsToggle(this)">
              <h5 class='details__title'>Деталі <i class="fas fa-sort-down"></i></h5>
              <ol class='details__list d-none'>
                <li>Викладання матеріалу<span>{q1}</span></li>
                <li>Контакт з аудиторією<span>{q2}</span></li>
                <li>Оцінювання навчальних досягнень<span>{q3}</span></li>
                <li>Культура мовлення<span>{q4}</span></li>
                <li>Стимулювання самостійних навчальних зусиль студентів<span>{q5}</span></li>
                <li>Рівень організованості<span>{q6}</span></li>
                <li>Педагогічна майстерність<span>{q7}</span></li>
                <li>Психологія спілкування<span>{q8}</span></li>
                <li>Зворотній зв’язок<span>{q9}</span></li>
                <li>Володіння сучасними технологіями навчання<span>{q10}</span></li>
              </ol>
            </div>
          </div>
"""

def handle_voting(login):
  students_collection = db['students']
  result = students_collection.find_one({"e-mail" : login})
  group_id = result['group']
  groups_collection = db['groups']
  group = groups_collection.find_one({"group_id" : group_id })
  n = ""
  b = False
  for i in range(len(group['list_of_teachers'])):
      name = group['list_of_teachers'][i][0]
      subject = group['list_of_teachers'][i][1]
      if name not in result["voted_to"]:
        n+=BIGSTR.format(name=name, subject=subject, login=login)

  if n == "":
    n = SPAN
    b = True

  original = open("voting.html", "r").read()
  return original.replace("REPLACEME", n), b

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
  
        query_string = None
    
        if '/voting' in self.path:
            query_components = parse.parse_qs(parse.urlparse(self.path).query)
            if 'email' in query_components:
                login = query_components["email"][0]
            result = None
            if login:
                original, b_voted = handle_voting(login)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(bytes(original, "utf8"))
                return

        if '/Vjzpfz1989' in self.path:
          collection = db ['teachers']
          teachers = collection.find()
          n = ""

          for teacher in teachers:
            name = teacher["name"]
            score = teacher["score"]
            try:
              q1 = teacher["sum_q1"]/teacher["num_q1"]
              q2 = teacher["sum_q2"]/teacher["num_q2"]
              q3 = teacher["sum_q3"]/teacher["num_q3"]
              q4 = teacher["sum_q4"]/teacher["num_q4"]
              q5 = teacher["sum_q5"]/teacher["num_q5"]
              q6 = teacher["sum_q6"]/teacher["num_q6"]
              q7 = teacher["sum_q7"]/teacher["num_q7"]
              q8 = teacher["sum_q8"]/teacher["num_q8"]
              q9 = teacher["sum_q9"]/teacher["num_q9"]
              q10 = teacher["sum_q10"]/teacher["num_q10"]
              n+=RESULTS_STR.format(name=name, score=score, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9, q10=q10)
            except:
              continue

          self.send_response(200)
          self.send_header("Content-type", "text/html")
          self.end_headers()

          original = open("results.html", "r").read()
          original = original.replace("REPLACEME_1", n)
          self.wfile.write(bytes(original, "utf8"))
          return

        if '/login' in self.path:
            collection = db['students']
            query_components = parse.parse_qs(parse.urlparse(self.path).query)
            if 'email' in query_components:
                login = query_components["email"][0]
            result = None
            if login:
                #this is the mongo query
                result = collection.find_one({"e-mail" : login})
                
                if result:
                    if result['voted'] == True:
            # TODO - move to a place where it will work on every page
                        self.send_response(200)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        original = open("voting.html", "r").read()
                        original = original.replace("REPLACEME", "<br><span>Ви вже проголосували!</span>")
                        self.wfile.write(bytes(str(original), "utf8"))
                        return
                    else:
                        self.send_response(301)
                        self.send_header('Location', f"/voting.html?email={login}")
                        self.end_headers()
                        return 
                else:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    original = open("voting.html", "r").read()
                    original = original.replace("REPLACEME", "<br><span>Будь ласка, введіть правильний e-mail!</span>")
                    self.wfile.write(bytes(str(original), "utf8"))
                    return

        fields = parse.parse_qs(query_string) if query_string else {}
        if fields:
            print ("e-mail = {}".format(fields.get('email')[0]))
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
  
        if '/voting' in self.path:
      # parse parameters from request body
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            fields = parse.parse_qs(body.decode('utf-8')) if body else {}
            collection = db['teachers']
            q1 = None
            q2 = None
            q3 = None
            q4 = None
            q5 = None
            q6 = None
            q7 = None
            q8 = None
            q9 = None
            q10 = None
            login = None
        
            if fields:
                q1 = int(fields.get('q1')[0])
                q2 = int(fields.get('q2')[0])
                q3 = int(fields.get('q3')[0])
                q4 = int(fields.get('q4')[0])
                q5 = int(fields.get('q5')[0])
                q6 = int(fields.get('q6')[0])
                q7 = int(fields.get('q7')[0])
                q8 = int(fields.get('q8')[0])
                q9 = int(fields.get('q9')[0])
                q10 = int(fields.get('q10')[0])
                t_name = str(fields.get('teacher_name')[0])
                print("***", t_name)
        # TODO - get the teacher name from fields
                teacher = collection.find_one({"name" : t_name})
                sum_q1 = teacher['sum_q1'] + q1
                sum_q2 = teacher['sum_q2'] + q2
                sum_q3 = teacher['sum_q3'] + q3
                sum_q4 = teacher['sum_q4'] + q4
                sum_q5 = teacher['sum_q5'] + q5
                sum_q6 = teacher['sum_q6'] + q6
                sum_q7 = teacher['sum_q7'] + q7
                sum_q8 = teacher['sum_q8'] + q8
                sum_q9 = teacher['sum_q9'] + q9
                sum_q10 = teacher['sum_q10'] + q10
                num_q1 = teacher['num_q1'] + 1
                num_q2 = teacher['num_q2'] + 1
                num_q3 = teacher['num_q3'] + 1
                num_q4 = teacher['num_q4'] + 1
                num_q5 = teacher['num_q5'] + 1
                num_q6 = teacher['num_q6'] + 1
                num_q7 = teacher['num_q7'] + 1
                num_q8 = teacher['num_q8'] + 1
                num_q9 = teacher['num_q9'] + 1
                num_q10 = teacher['num_q10'] + 1
                collection.update_one(
                  {"name" : t_name},
                  {"$set": {"sum_q1": sum_q1, "sum_q2": sum_q2, "sum_q3": sum_q3, "sum_q4": sum_q4, "sum_q5": sum_q5, "sum_q6": sum_q6, "sum_q7": sum_q7, "sum_q8": sum_q8, "sum_q9": sum_q9, "sum_q10": sum_q10, "num_q1": num_q1, "num_q2": num_q2, "num_q3": num_q3, "num_q4": num_q4, "num_q5": num_q5, "num_q6": num_q6, "num_q7": num_q7, "num_q8": num_q8, "num_q9": num_q9, "num_q10": num_q10}}
                )
                try:
                  score = ((sum_q1/num_q1)+(sum_q2/num_q2)+(sum_q3/num_q3)+(sum_q4/num_q4)+(sum_q5/num_q5)+(sum_q6/num_q6)+(sum_q7/num_q7)+(sum_q8/num_q8)+(sum_q9/num_q9)+(sum_q10/num_q10))/10
                  collection.update_one(
                    {"name" : t_name},
                    {"$set": {"score": score}})
                except:
                  pass

            query_components = parse.parse_qs(parse.urlparse(self.path).query)
            if 'email' in query_components:
              login = query_components["email"][0]

            elif 'email' in fields:
              login = fields["email"][0]
            else:
              print("BUGGG")
            students_collection = db['students']
            #result = students_collection.find_one({"e-mail" : login})
            students_collection.update_one({"e-mail" : login}, {"$push": {"voted_to": t_name}})
        if login:
          original, b_voted = handle_voting(login)
          if b_voted:
            students_collection.update_one({"e-mail" : login}, {"$set": {"voted": True}})
          # TODO - hadle "setting off the votes"
          # logic:  1. find the "teacher name"
          #      2. find the button after it
          #      3. change it to a span of "already voted"
          #f_index = original.find(t_name)  
          #f_index = original.find(BUTTON)
          #original.replace(original[f_index:f_index+len(BUTTON)], SPAN)
          print("end of post func")
          self.send_response(200)
          self.send_header('Content-type','text/html')
          self.end_headers()
          self.wfile.write(bytes(original, "utf8"))
          return
        # Send the http body == html
        #self.wfile.write(bytes(str("Added your vote"), "utf8"))
        return

if __name__ == '__main__':
    HTTPServer(('', 8008), CustomHTTPRequestHandler).serve_forever()
