# 作业评分辅助工具 (Assignment Grading Tool)

这是一个基于Web的作业评分辅助工具，是自用的作业批改辅助工具

## 主要功能

1. **进制转换**
   - 将十进制数转换为二进制
   - 将十进制数转换为十六进制
   - 提供详细的转换步骤说明

2. **无符号二进制和十六进制运算**
   - 二进制加法运算（带进位显示）
   - 十六进制加法运算（带进位显示）

3. **二进制补码运算**
   - 十进制负数转二进制补码
   - 二进制补码加法运算（带溢出检测）

4. **ASCII编码转换**
   - 将输入的姓名转换为ASCII十六进制表示
   - 计算所需的比特数

## 使用方法

1. 访问工具网页：[Assignment Grading Tool](https://waynez.online/)

2. 输入学号
   - 在"ID"输入框中输入你的学号
   - 系统会自动提取学号中最后两个非零数字作为基础数值A
   - 如果找不到两个非零数字，将使用默认值11

3. 查看计算结果
   - 所有计算结果会实时更新
   - 每个计算步骤都有详细说明

4. 输入姓名（用于ASCII转换）
   - 在姓名输入框中输入你的全名
   - 系统会自动转换为ASCII十六进制表示

## AI编程感想

1. **编程基础依然重要**
   - 如果完全不懂代码，面对稍复杂的项目就会失控。AI可能在错误的地方反复生成问题代码，而缺乏知识储备的话将无法识别错误根源，难以有效指导AI修正，可能陷入僵局

2. **前期架构设计**
   - 项目初期应由人明确模块划分和交互逻辑，降低模块间耦合度。这样即使后续出现Bug，影响范围也能控制在单个模块内，避免因连锁反应导致全面崩溃

3. **重构可能比修补更高效**
   - 当AI生成的代码出现结构性错误时，与其在错误基础上反复调整，不如直接删除问题模块，用更清晰的思路重新描述需求让AI重构

4. **错误处理可以分阶段实施**
   - AI生成的冗余错误处理代码可能成为新问题的源头。建议先集中实现核心功能链路，待主流程稳定后再逐步补充异常处理，避免过早引入复杂判断干扰调试

5. **需求需要分层转化**
   - 直接让AI写代码容易误解需求，可先用一个AI将模糊需求转化为技术文档（例如："请帮我把‘做个文章分析工具’翻译成程序员能理解的需求"），再用整理后的文档指导另一个AI编码，能减少沟通偏差

6. **企业级应用仍存在障碍**
   - 当前AI难以应对商业项目需求：代码安全性无法保障（如敏感信息泄露）、复杂业务规则理解困难（如行业特例逻辑）、长期维护时无法保持代码一致性，这些领域仍然离不开人

7. **个人开发正迎来变革**
   - 普通人用AI实现自动化脚本、小工具已非常可行，比如自动整理文件、批量处理数据等场景，普通人无需深入编程即可快速验证创意，这是未曾出现的巨大变革

8. **未来人机协作模式**
   - 随着使用经验积累，AI编程也许发展出分层协作模式，人类把控架构设计、核心算法和关键模块，AI负责实现工具函数、模板代码和文档生成

ALL IN AI
