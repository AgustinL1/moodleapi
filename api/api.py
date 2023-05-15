from flask import Flask, request
from flask_lt import run_with_lt
from db_manager import DBManager
import json
import time
import bcrypt
import os

api_subdomain = os.getenv("API_SUBDOMAIN")
app = Flask(__name__)
run_with_lt(app, subdomain=api_subdomain)

@app.route('/', methods = ['GET'])
def index():
   return "MOODLE API", 200


@app.route('/insertar-mensaje', methods = ['PUT'])
def insertar():
   print("hola")
   print(request)
   try:
      discussion = request.json.get("discussion")
      userId = request.json.get("userId")
      msg = request.json.get("msg")
      subject = request.json.get("subject")
   except:
      return "", 400

   created = int(time.time())
   wordcount = len(msg.split())
   charcount = len(msg)
   msg = '<div class="text_to_html">' + msg + '</div>'

   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "INSERT INTO mdl_forum_posts (discussion, parent, userid, created, subject, message, wordcount, charcount) VALUES (?,(select min(fp.id) from mdl_forum_posts fp where fp.discussion = ?),?,?,?,?,?,?)",
      (discussion, discussion, userId, created, subject, msg, wordcount, charcount)
   )
   DBManager.get_instance().commit()
   return "", 200


@app.route('/obtener-foros', methods = ['GET'])
def obtenerForos():
   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "SELECT mf.id, mf.course, mf.name FROM mdl_forum mf",
      ()
   )

   res = []

   for i in cur:
      res.append({"id":i[0],"course":i[1],"name":i[2]})

   return json.dumps(res)

@app.route('/obtener-discusiones', methods = ['GET'])
def obtenerDisuciones():
   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "SELECT mfd.id, mfd.course , mfd.forum, mfd.name FROM mdl_forum_discussions mfd",
      ()
   )

   res = []

   for i in cur:
      res.append({"id":i[0],"course":i[1],"forum":i[2],"name":i[3]})

   return json.dumps(res)

@app.route('/obtener-quizzes', methods = ['GET'])
def obtenerQuizzes():
   try:
        course = request.json.get("course")
   except:
        return "", 400
   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "SELECT mdq.id, mdq.course, mdq.name, mdq.intro \
      FROM mdl_quiz mdq \
      where(mdq.course=?)",
      (course,))

   res = []

   for i in cur:
      res.append({"id":i[0],"course":i[1],"name":i[2],"intro":i[3]})

   return json.dumps(res)
   
@app.route('/obtener-mensajes-discusion', methods = ['GET'])
def obtenerMensajesForos():
   print(request.json)
   try:
      discussion = request.json.get("discussion")
   except:
      return "", 400

   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "SELECT mfp.id, mfp.discussion, mfp.parent, mfp.userid, mfp.created, mfp.subject, mfp.message FROM mdl_forum_posts mfp WHERE mfp.discussion=?",
      (discussion,)
   )

   res = []

   for i in cur:
      res.append({"id":i[0],"discussion":i[1],"parent":i[2],"userId":i[3],"created":i[4],"subject":i[5],"message":i[6]})

   return json.dumps(res)


@app.route('/obtener-datos-foro', methods = ['GET'])
def obtenerDatosForo():

   try:
      name = request.json.get("name")
   except:
      return "", 400

   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "SELECT mf.id, mf.course, mf.intro FROM mdl_forum mf WHERE  mf.name=?",
      (name,)
   )

   res = []

   for i in cur:
      res.append({"id":i[0],"course":i[1],"intro":i[2]})

   return json.dumps(res)


@app.route('/user-login', methods = ['PUT'])
def userLogin():

   try:
      username = request.json.get("username")
      password = request.json.get("password")
   except:
      return "", 400

   
   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "SELECT md.id,md.password,md.username,md.firstname,md.lastname,md.email FROM mdl_user md WHERE  md.username=?",
      (username,)
   )

   res = []
   
   for i in cur:
      res.append({"id":i[0],"username":i[2],"firstname":i[3],"lastname":i[4],"email":i[5]})
   
   if(bcrypt.checkpw(password.encode(),i[1].encode())):
      return json.dumps(res)
   else:
      return json.dumps([])


@app.route('/obtener-nombre-discusion', methods = ['GET'])
def obtenerNombreDiscusion():

   try:
      id = request.json.get("id")
   except:
      return "", 400

   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "SELECT mfd.name FROM mdl_forum_discussions mfd WHERE mfd.id=?",
      (id,)
   )

   res = []

   for i in cur:
      res.append({"name":i[0]})

   return json.dumps(res)

   
@app.route('/obtener-participantes-curso', methods = ['GET'])
def obtenerParticipantesCurso():

   try:
      courseId = request.json.get("courseId")
   except:
      return "", 400

   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "SELECT ue.userid FROM mdl_course AS c JOIN mdl_enrol AS en ON en.courseid = c.id JOIN mdl_user_enrolments AS ue ON ue.enrolid = en.id WHERE c.id=?",
      (courseId,)
   )

   res = []

   for i in cur:
      res.append({"userId":i[0]})

   return json.dumps(res)




@app.route('/obtener-preguntas-examen', methods = ['GET'])
def obtenerPreguntasExamen():

   try:
      id = request.json.get("id")
   except:
      return "", 400

   cur = DBManager.get_instance().get_cur()
   cur.execute(
      """
         SELECT q.id,q.course,q.name,q.timelimit,q.intro
               ,sumgrades,grade,quizid,questionid,qe.name,questiontext
               ,defaultmark,qa.id,answer,fraction,c.fullname, c.shortname, c.summary, qa.feedback, qe.generalfeedback
         FROM mdl_quiz q
         join mdl_quiz_slots qs on q.id = qs.quizid
         join mdl_question qe on qe.id = qs.questionid
         join mdl_question_answers qa on qe.id = qa.question
         join mdl_course c on c.id = q.course
         where q.id = ?""",
      (id,)
   )

   res = []

   for i in cur:
      res.append({"id":i[0],"course":i[1], "name":i[2],"timelimit":i[3], "intro":i[4],
                  "sumgrades":float(i[5]),"grade":float(i[6]),"quizid":i[7],"questionid":i[8],
                  "question_name":i[9],"question_text":i[10],"defaultmark":float(i[11]),"question_answer_id":i[12],
                  "question_answer":i[13],"fraction":float(i[14]), "fullName":i[15], "shortName":i[16], 
                  "summary":i[17], "feedback":i[18], "generalfeedback":i[19]})

   return json.dumps(res)


@app.route('/insertar-intento-quiz', methods = ['PUT'])
def insertarIntentoQuiz():

   try:
      quiz = request.json.get("quiz")
      userid = request.json.get("userid")
      layout = request.json.get("layout")
      timestart = request.json.get("timestart")
      timefinish = request.json.get("timefinish")
      sumgrades = request.json.get("sumgrades")
   except:
      return "", 400

   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "insert into mdl_question_usages (contextid, component, preferredbehaviour) values  (1,'mod_quiz', 'deferredfeedback')",
   )
   DBManager.get_instance().commit()
   cur.execute(
      "insert into mdl_quiz_attempts (quiz, userid, attempt, uniqueid, layout, currentpage, preview, state,timestart, timefinish, timemodified, timemodifiedoffline,sumgrades) values(?,?,1,(select max(id) from mdl_question_usages),?,0,1,'finished',?,?,?,?,?)",
      (quiz,userid,layout,timestart,timefinish,timefinish,timefinish,sumgrades)
   )

   DBManager.get_instance().commit()

   return "", 200


@app.route('/obtener-leccion', methods = ['GET'])
def obtenerRespuestasLesson():

   try:
      id = request.json.get("id")
   except:
      return "", 400

   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "SELECT lp.id, lp.prevpageid, lp.nextpageid, lp.qtype, lp.contents, la.id, la.jumpto, la.score, la.answer, la.response FROM mdl_lesson_pages lp JOIN mdl_lesson_answers la ON lp.lessonid = la.lessonid AND lp.id = la.pageid WHERE la.lessonid = ?;",
      (id,)
   )

   res = []

   for i in cur:
      res.append({"pageId":i[0], "prevPageId":i[1], "nextPageId":i[2],"qType":i[3], "contents":i[4], "answerId":i[5],"jumpTo":i[6], "score":i[7], "answer":i[8], "response":i[9]})
   return json.dumps(res)


@app.route('/insertar-intento-lesson', methods = ['PUT'])
def insertarIntentoLesson():

   try:
      lessonId = request.json.get("lessonId")
      pageId = request.json.get("pageId")
      userid = request.json.get("userid")
      answerId = request.json.get("answerId")
      correct = request.json.get("correct")
      userAnswer = request.json.get("userAnswer")
      timeSeen = request.json.get("timeSeen")
   except:
      return "", 400

   cur = DBManager.get_instance().get_cur()
   cur.execute(
      "insert into mdl_lesson_attempts (lessonid, pageid, userid, answerid, retry, correct, useranswer, timeseen) values  (?, ?, ?, ?, 0, ?, ?, ?);",
      (lessonId,pageId,userid,answerId,correct,userAnswer,timeSeen)
   )

   DBManager.get_instance().commit()

   return "", 200

@app.route('/obtener-videos', methods=['GET'])
def obtenerVideo():
    print(request.json)
    try:
        course = request.json.get("course")
    except:
        return "", 400

    cur = DBManager.get_instance().get_cur()
    cur.execute("select distinct u.name, u.externalurl \
               from mdl_url u \
               join mdl_course_modules cm on u.id=cm.instance \
               join mdl_course_sections cs on cm.section=cs.id \
               where(u.course=?)",
                (course,))
    res = []
    for i in cur:
        res.append({"name": i[0], "externalurl": i[1]})
   
    # Convertir el objeto JSON en una cadena
    return json.dumps(res)

@app.route('/obtener-cursos', methods=['GET'])
def obtenerCursos():
   
   cur = DBManager.get_instance().get_cur()
   cur.execute("select c.id, c.fullname \
               from mdl_course c \
               where c.id <> 1")   
   res = []
   for i in cur:
      res.append({
         "id": i[0],
         "fullname": i[1]
      })
   
   return json.dumps(res)

if __name__ == '__main__':
   DBManager.get_instance()
   app.run(debug=True, host="0.0.0.0")