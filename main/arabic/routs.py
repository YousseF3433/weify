from main.models import Por, Blog, Question, Cat
from main import db
from .translation import translation
from . import ar_bp

from flask import render_template, request
from sqlalchemy import desc


@ar_bp.route("/")
@ar_bp.route("/index")
def index():
  por = Por.query.order_by(desc(Por.id)).limit(2).all()
  blogs = Blog.query.order_by(desc(Blog.id)).limit(3).all()
  return render_template("ar-index.html", title="الصفحة الرئيسية - ويبفاي | الشركة الرائدة في تصميم وتطوير المواقع في مصر",
                         des="مرحبًا بك في ويبفاي، شركتك الموثوقة في تصميم المواقع وتطويرها في مصر. نحن متخصصون في تصميم المواقع المخصص، حلول التجارة الإلكترونية، وتحسين محركات البحث لمساعدة عملك على النجاح عبر الإنترنت. ابدأ معنا اليوم!",
                         blogs=blogs, 
                         pors=por,
                         translation=translation
                        )

@ar_bp.route("/about")
def about():
  return render_template("ar-about.html", title="عن الشركة - ويبفاي | خبراء تصميم وتطوير المواقع في مصر",
                         des="تعرف على ويبفاي، الشركة الرائدة في تصميم وتطوير المواقع في مصر. نحن متخصصون في تصميم المواقع المخصص، حلول التجارة الإلكترونية، وتحسين محركات البحث لمساعدة الشركات على النجاح عبر الإنترنت. اكتشف قصتنا ورؤيتنا وكيف يمكننا تحقيق رؤيتك.")

@ar_bp.route("/faq")
def faq():
   return render_template("ar-faq.html", title="الأسئلة الشائعة - ويبفاي | الأسئلة الشائعة حول تصميم وتطوير المواقع",
                          des="إجابة على الأسئلة الشائعة حول خدمات تصميم وتطوير المواقع الخاصة بنا. تعرف على عملية العمل لدينا، التسعير، وكيف يمكن لويبفاي مساعدتك في تحقيق رؤيتك للموقع.",
                          questions = Question.query.all(),
                          translation=translation
                          )

@ar_bp.route("/contact")
def contact():
  return render_template("ar-contact.html", title="اتصل بنا - ويبفاي | تواصل مع فريق تطوير المواقع لدينا",
   des="هل لديك أسئلة أو تحتاج إلى عرض أسعار؟ اتصل بويبفاي اليوم للحصول على خدمات تصميم وتطوير المواقع. نحن هنا لمساعدتك في جميع احتياجاتك المتعلقة بحلول الويب. تواصل معنا وابدأ مشروعك معنا!",
  )

@ar_bp.route("/blogs")
def blogs():
  page = request.args.get("page", 0, type=int) * 6
  return render_template("ar-blogs.html", title="مدونات تصميم وتطوير المواقع - ويبفاي | رؤى ونصائح الخبراء",
                         des="استعرض مدوناتنا للحصول على نصائح الخبراء في تصميم وتطوير المواقع، أحدث الاتجاهات وأفضل الممارسات. ابقَ على اطلاع بأفكار قيمة لمساعدتك في بناء مواقع أفضل وتحسين وجودك عبر الإنترنت. ويبفاي – شريكك لحلول الويب الاحترافية",
                         blogs=Blog.query.all()[page: page + 10], page=page // 6, translation=translation)

@ar_bp.route("/blog/<int:id>")
def blog(id):
  blog = db.session.get(Blog, id)
  return render_template("ar-blog.html", title=f"المدونة - {translation(blog.title)}", # type: ignore
                          des=translation(blog.shor_description), # type: ignore
                          blog=blog, translation=translation)

@ar_bp.route("/portfolio")
def portfolio():
  return render_template("ar-portfolio.html" , title="سابقه الاعمال - ويبفاي | مشاريعنا في تصميم وتطوير المواقع",
                         des="استعرض سوابق الاعمال ويبفاي لعرض مشاريع تصميم وتطوير المواقع الناجحة. شاهد كيف ساعدنا الشركات في بناء مواقع مخصصة وحلول للتجارة الإلكترونية والمزيد.",
                         pors = Por.query.all(),
                         cats=Cat.query.all(),
                         translation=translation)

@ar_bp.route("/pricing")
def pricing():
  mode = request.args.get("mode") 
  active = request.args.get("active")
  return render_template("ar-pricing.html", title="التسعير - ويبفاي | باقات تصميم وتطوير مواقع بأسعار معقولة",
                         des="استعرض تسعير ويبفاي الشفاف لخدمات تصميم وتطوير المواقع وتحسين محركات البحث. اختر الباقة المثالية لتناسب احتياجاتك وميزانيتك، سواء كنت بحاجة إلى موقع بسيط أو حل تجارة إلكترونية شامل.",
                         mode=mode,
                         active=active
                        )
  
@ar_bp.route("/services")
def services():
  return render_template("ar-services.html", title="خدمات تصميم وتطوير المواقع | التجارة الإلكترونية، تحسين محركات البحث، الاستضافة والمزيد", des="استكشف خدماتنا الاحترافية في تصميم المواقع، تطوير التجارة الإلكترونية، تحسين محركات البحث، والاستضافة الموثوقة. نحن نقدم حلولًا مخصصة لمساعدتك في نجاح عملك على الإنترنت.")