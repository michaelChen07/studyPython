#encoding=utf-8
import re

#匹配连续5个数字，前后不是数字或只有5个数字。结果中只包含数字

rule = r'\D\d{5}\D|^\d{5}\D|\D\d{5}$|^\d{5}$'
def test_regular(rule,destine_string):
    result=re.search(rule,destine_string)
    if result:
        word_list=[]
        for s in result.group():
            if s in "0123456789":
                word_list.append(s)
        print "".join(word_list)
        return "".join(word_list)

    else:
        print "not found!"
        return None

#测试
if __name__=="__main__":#当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行
    #assert test_regular(rule,"12345")=="12345"#断言，正确则继续执行，错误则停止
    #assert test_regular(rule,"12345 ")=="12345"
    #assert test_regular(rule," 12345")=="12345"
    #assert test_regular(rule,"x12345x")=="12345"
    #assert test_regular(rule,"112345") == None
    #assert test_regular(rule,"x123c45x")== None
    test_data = []
    with open("test2.txt","r") as fp:
        for content in fp.readlines():
            #test_data.append(content.strip("\n"))
            assert test_regular(rule, content.strip("\n")) == None

    #test_data = ["112345", "1234", "t1234","1234 "]
    for data in test_data:
        assert test_regular(rule,data) == None

    print "test completed!"

#代码覆盖率指标：语言覆盖、条件覆盖、判定覆盖、路径覆盖
#数据驱动：相同的测试用例，用不同的数据来执行
