from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pathlib import Path

out=Path('商城交互说明文档.docx')
doc=Document(); sec=doc.sections[0]; sec.top_margin=Inches(.7); sec.bottom_margin=Inches(.7); sec.left_margin=Inches(.8); sec.right_margin=Inches(.8)
styles=doc.styles
styles['Normal'].font.name='Microsoft YaHei'; styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft YaHei'); styles['Normal'].font.size=Pt(10.5)
for s,size in [('Title',24),('Heading 1',16),('Heading 2',13)]:
 st=styles[s]; st.font.name='Microsoft YaHei'; st._element.rPr.rFonts.set(qn('w:eastAsia'),'Microsoft YaHei'); st.font.size=Pt(size); st.font.bold=True; st.font.color.rgb=RGBColor(0,0,0)

def shade(cell,fill):
 tcPr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),fill); tcPr.append(shd)
def table(headers,rows):
 t=doc.add_table(rows=1, cols=len(headers)); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.style='Table Grid'
 for i,h in enumerate(headers):
  c=t.rows[0].cells[i]; c.text=h; shade(c,'E85B45'); c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
  for r in c.paragraphs[0].runs: r.font.bold=True; r.font.color.rgb=RGBColor(255,255,255)
 for row in rows:
  cells=t.add_row().cells
  for i,v in enumerate(row): cells[i].text=v; cells[i].vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
 return t

t=doc.add_paragraph(); t.style='Title'; t.alignment=WD_ALIGN_PARAGRAPH.CENTER; t.add_run('福聚贡翔商城交互说明文档')
p=doc.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; p.add_run('基于本地 HTML 交互原型整理 | 版本 1.0 | 2026-11-23').italic=True

doc.add_heading('一 文档目的与范围',1)
doc.add_paragraph('本文档用于说明福聚贡翔商城本地交互原型的页面结构、用户路径、操作反馈和业务状态。内容依据 fujugongxiang-miniapp 目录下的 HTML 页面、链接关系、按钮事件和页面脚本整理，可作为产品评审、前端联调和测试用例编写的基础。')
doc.add_paragraph('原型以移动端商城为主，覆盖消费者购物、社交消息、售后服务、批发选品、分销，以及商家经营后台。页面目前以演示数据和前端跳转为主，部分提交、支付、定位、上传和消息能力通过 Toast 或静态状态模拟。')

doc.add_heading('二 产品信息架构',1)
table(['模块','入口页面','核心能力'],[
('消费者商城','home.html、category.html、search.html','首页浏览、分类筛选、搜索、附近店、秒杀、拼单'),
('商品与店铺','product-detail.html、shop.html、coupons.html','商品详情、规格选择、收藏分享、加入购物车、立即购买、领券'),
('交易链路','order-confirm.html、payment.html、orders.html','确认订单、地址、优惠、发票、支付、订单状态与物流'),
('售后服务','aftersale-apply.html、aftersale-list.html、aftersale-detail.html','售后申请、审核、寄回、签收、退款、平台介入'),
('社交与客服','messages.html、chat-shop.html、chat-service.html、friends.html','好友、店铺客服、平台客服、商品卡和订单卡分享'),
('分销与钱包','distribution.html、distribution-products.html、wallet.html','分销商品、佣金、提现、推广订单'),
('批发选品','wholesale.html、wholesale-shop.html、wholesale-pick-orders.html','批发选品、加入选品单、在线/线下订单'),
('商家后台','merchant-workbench.html、merchant-orders.html、merchant-goods.html','经营概览、商品、订单、售后、营销、入驻')])

doc.add_heading('三 全局交互规范',1)
for x in ['底部主导航固定为首页、附近、批发、消息、我的，当前页面通过高亮态标识所在模块。','返回按钮通常回到上一级业务页面，右侧文字入口用于进入规则、管理或相关列表。','主要操作使用橙红色按钮或渐变按钮，次要操作使用浅色描边按钮。','筛选项、状态标签和营销类型采用横向 Chips，点击后切换 on 状态并更新列表或详情内容。','数量控件使用减号、数量、加号组合，数量下限通常为 1。','演示动作通过 Toast 给出结果，例如已复制、已保存、已提醒商家或演示环境限制。','危险操作如删除地址、撤销售后、清空记录需要单独按钮，成功后刷新当前列表或关闭当前工单。']:
 doc.add_paragraph(x,style='List Bullet')

doc.add_heading('四 消费者购物主流程',1)
doc.add_heading('4.1 浏览与找商品',2)
doc.add_paragraph('用户从首页进入搜索、分类、附近店、限时秒杀或拼单专场。搜索页支持输入关键词并提交，历史记录页支持查看和清空历史。分类页通过一级类目和商品列表完成筛选。附近店展示门店距离、营业信息和进店入口。')
doc.add_heading('4.2 商品详情与店铺',2)
doc.add_paragraph('商品详情页承载商品图片、标题、价格、销量、规格、库存、评价和店铺信息。用户可选择规格和数量，执行收藏、分享、加入购物车或立即购买。店铺首页提供商品浏览、优惠券领取、客服入口和进店后的继续购买路径。')
doc.add_heading('4.3 下单与支付',2)
table(['步骤','页面','主要交互','结果'],[
('确认信息','order-confirm.html','选择收货地址、商品数量、优惠券、平台红包、发票；填写备注','计算应付金额'),
('地址管理','address.html、address-edit.html','选择地址、设默认、编辑、删除、新增、地图选点和重新定位','返回确认订单并带回地址'),
('支付','payment.html','选择支付方式并提交支付','进入订单详情或显示支付结果'),
('订单跟踪','orders.html、order-detail.html、logistics.html','按待付款、待发货、待收货、已完成等状态筛选','查看物流、确认收货、评价或申请售后')])

doc.add_heading('五 售后与客服流程',1)
doc.add_paragraph('售后从订单详情进入申请页，用户选择售后类型、问题描述、数量和凭证后提交。售后列表按全部、待审核、待寄回、待签收、待退款、已完成筛选。售后详情根据状态动态展示截止时间、关联订单、物流填写、撤销、修改申请、催商家、联系客服、申请平台介入等操作。')
doc.add_paragraph('店铺客服支持快捷问答、文字发送、语音、表情、图片、拍照、商品卡和订单卡发送。平台客服提供订单、退款、入驻、佣金提现等快捷入口，并支持转人工客服。')

doc.add_heading('六 分销与批发流程',1)
doc.add_paragraph('分销中心展示累计佣金、待入账和可提现金额，分销商品页支持按全部、高佣金、销量优先、新品筛选。商品卡展示售价、一级分销佣金和销量，点击进入商品详情。佣金钱包提供收入明细和提现入口。')
doc.add_paragraph('批发模块从批发选品进入批发店铺和商品详情，用户可将商品加入选品订单，编辑数量后确认下单信息。订单区分当前订单、待确认、在线支付、已发货等状态，并提供批发评价和私域评论。')

doc.add_heading('七 商家后台流程',1)
table(['业务域','页面与交互','关键状态'],[
('工作台','merchant-workbench.html','经营概览、待处理事项、快捷入口'),
('商品管理','merchant-goods.html、merchant-goods-edit.html、merchant-category-pick.html','商品列表、上架/下架、编辑、选择类目'),
('订单管理','merchant-orders.html、merchant-order-detail.html','订单筛选、发货、确认收款、查看详情'),
('售后处理','merchant-aftersale.html','审核售后、同意/拒绝、处理退款'),
('营销工具','merchant-marketing.html','促销、秒杀、礼品金、分销活动的创建和管理'),
('活动创建','merchant-promotion-new.html、merchant-seckill-new.html、merchant-coupon-new.html、merchant-distribution-new.html','填写规则、选择商品/类目、发布或存草稿'),
('入驻','merchant-apply.html','填写主体资料、联系人、类目、资质并提交审核')])

doc.add_heading('八 页面清单与验收重点',1)
doc.add_paragraph('消费者页面包括 home、category、search、nearby、seckill、group-buy、product-detail、shop、coupons、platform-coupons、my-coupons、history、post、profile、settings、service。交易页面包括 order-confirm、payment、orders、order-detail、logistics、review、invoice、address、address-edit。')
doc.add_paragraph('验收时重点检查页面跳转是否符合上表入口关系，筛选状态是否唯一高亮，数量和金额是否联动，地址和优惠是否能回传确认订单，售后状态切换后底部操作是否同步变化，Toast 是否在操作后出现，以及底部导航在各主模块是否保持一致。')

doc.add_heading('九 当前原型边界',1)
doc.add_paragraph('当前页面主要用于交互展示。支付、真实库存、地图定位、文件上传、消息服务、物流接口、订单持久化和权限校验尚未接入真实后端。联调阶段需要补充接口字段、异常码、加载态、空态、网络失败态和重复提交防护。')

doc.save(out)
print(out.resolve())
