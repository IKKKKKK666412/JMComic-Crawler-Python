from jmcomic import *
from jmcomic.cl import JmcomicUI

# 下方填入你要下载的本子的id，一行一个，每行的首尾可以有空白字符
jm_albums = '''
JM539434
539434
JM624396
624396
JM624379
624379
JM315992
315992
JM338363
338363
JM276417
276417
JM275888
275888
JM276271
276271
JM274631
274631
JM271956
271956
JM253591
253591
JM292614
292614
JM457193
457193
JM275155
275155
JM274745
274745
JM271619
271619
JM272409
272409
JM229433
229433
JM231574
231574
JM251291
251291
JM270429
270429
JM273005
273005
JM269920
269920
JM288660
288660
JM314457
314457
JM518078
518078
JM521404
521404
JM270170
270170
JM270745
270745
JM270841
270841
JM270390
270390
JM138326
138326
JM202105
202105
JM219408
219408
JM270193
270193
JM208185
208185
JM368177
368177
JM512458
512458
JM186557
186557
JM592701
592701
JM263508
263508
JM498865
498865
JM213964
213964
JM223542
223542
JM263456
263456
JM414159
414159
JM441708
441708
JM441882
441882
JM479805
479805
JM484389
484389
JM259011
259011
JM259010
259010
JM259528
259528
JM597886
597886
JM245595
245595
JM257613
257613
JM563711
563711
JM256940
256940
JM256478
256478
JM463454
463454
JM321505
321505
JM254910
254910
JM254913
254913
JM254915
254915
JM255221
255221
JM428644
428644
JM34865
34865
JM59202
59202
JM255293
255293
JM255938
255938
JM444924
444924
JM457734
457734
JM255014
255014
JM619532
619532
JM186357
186357
JM420341
420341
JM253597
253597
JM253836
253836
JM105986
105986
JM251851
251851
JM251944
251944
JM425017
425017
JM511353
511353
JM250557
250557
JM349977
349977
JM26672
26672
JM4823
4823
JM246354
246354
JM499813
499813
JM148215
148215
JM246877
246877
JM37342
37342
JM103032
103032
JM248321
248321
JM369407
369407
JM177667
177667
JM496895
496895
JM245413
245413
JM245795
245795
JM249712
249712
JM288609
288609
JM9121
9121
JM17640
17640
JM37022
37022
JM194349
194349
JM196309
196309
JM207765
207765
JM231985
231985
JM241306
241306
JM245972
245972
JM250594
250594
JM251855
251855
JM294806
294806
JM293861
293861
JM246263
246263
JM439649
439649
JM309622
309622
JM333020
333020
JM270004
270004
JM244643
244643
JM243119
243119
JM243101
243101
JM10433
10433
JM62607
62607
JM20807
20807
JM149693
149693
JM226029
226029
JM243679
243679
JM248171
248171
JM313481
313481
JM397303
397303
JM483253
483253
JM529911
529911
JM620892
620892
JM243864
243864
JM215902
215902
JM235788
235788
JM240472
240472
JM258777
258777
JM266191
266191
JM467095
467095
JM178129
178129
JM211753
211753
JM225811
225811
JM242006
242006
JM613000
613000
JM127261
127261
JM129858
129858
JM148674
148674
JM179333
179333
JM188470
188470
JM241467
241467
JM262885
262885
JM271434
271434
JM369428
369428
JM379603
379603
JM392340
392340
JM392452
392452
JM449867
449867
JM533201
533201
JM570518
570518
JM37097
37097
JM40115
40115
JM40275
40275
JM123772
123772
JM121312
121312
JM178778
178778
JM241287
241287
JM553009
553009
JM240163
240163
JM423392
423392
JM239788
239788
JM362445
362445
JM193306
193306
JM239740
239740
JM238560
238560
JM37671
37671
JM4735
4735
JM26208
26208
JM237190
237190
JM231956
231956
JM231805
231805
JM220219
220219
JM232256
232256
JM232100
232100
JM9981
9981
JM550185
550185
JM418500
418500
JM231397
231397
JM230580
230580
JM230193
230193
JM229976
229976
JM230005
230005
JM229965
229965
JM229434
229434
JM229435
229435
JM229584
229584
JM229808
229808
JM227369
227369
JM226747
226747
JM225603
225603
JM225598
225598
JM224563
224563
JM223665
223665
JM224272
224272
JM224354
224354
JM222880
222880
JM222605
222605
JM222468
222468
JM222453
222453
JM221146
221146
JM221426
221426
JM221442
221442
JM221661
221661
JM221420
221420
JM221346
221346
JM221295
221295
JM221111
221111
JM220764
220764
JM220765
220765
JM220447
220447
JM220272
220272
JM219693
219693
JM219324
219324
JM219320
219320
JM218362
218362
JM218350
218350
JM217628
217628
JM217724
217724
JM218141
218141
JM217586
217586
JM217484
217484
JM217081
217081
JM216633
216633
JM216646
216646
JM216647
216647
JM215814
215814
JM215678
215678
JM215786
215786
JM215463
215463
JM215152
215152
JM214824
214824
JM214605
214605
JM196014
196014
JM214432
214432
JM214514
214514
JM214401
214401
JM214398
214398
JM214078
214078
JM214079
214079
JM213958
213958
JM213930
213930
JM213448
213448
JM213228
213228
JM212997
212997
JM213082
213082
JM212924
212924
JM212040
212040
JM211240
211240
JM210264
210264
JM209824
209824
JM209181
209181
JM209180
209180
JM208992
208992
JM208964
208964
JM208596
208596
JM207970
207970
JM208008
208008
JM208085
208085
JM207572
207572
JM207300
207300
JM207291
207291
JM207119
207119
JM207118
207118
JM207057
207057
JM206963
206963
JM206708
206708
JM206522
206522
JM206521
206521
JM205535
205535
JM205612
205612
JM203023
203023
JM202978
202978
JM202695
202695
JM201160
201160
JM201563
201563
JM201709
201709
JM201739
201739
JM202061
202061
JM200636
200636
JM200627
200627
JM200350
200350
JM200536
200536
JM200307
200307
JM199743
199743
JM199619
199619
JM198921
198921
JM198911
198911
JM198358
198358
JM198011
198011
JM198566
198566
JM198054
198054
JM196852
196852
JM195698
195698
JM196257
196257
JM195459
195459
JM195693
195693
JM195512
195512
JM194636
194636
JM194495
194495
JM194347
194347
JM193398
193398
JM192868
192868
JM192870
192870
JM193288
193288
JM191991
191991
JM191990
191990
JM191767
191767
JM191756
191756
JM191131
191131
JM191114
191114
JM190539
190539
JM188750
188750
JM188636
188636
JM188490
188490
JM188477
188477
JM188589
188589
JM187787
187787
JM188418
188418
JM185073
185073
JM182239
182239
JM181614
181614
JM181509
181509
JM181363
181363
JM181067
181067
JM181034
181034
JM181010
181010
JM180834
180834
JM180609
180609
JM180772
180772
JM180628
180628
JM180535
180535
JM180284
180284
JM180043
180043
JM179847
179847
JM179634
179634
JM178811
178811
JM178191
178191
JM178441
178441
JM178033
178033
JM178002
178002
JM177892
177892
JM168048
168048
JM160061
160061
JM152332
152332
JM154577
154577
JM151966
151966
JM151809
151809
JM151664
151664
JM151711
151711
JM151790
151790
JM151438
151438
JM151064
151064
JM151355
151355
JM150029
150029
JM150097
150097
JM149977
149977
JM149987
149987
JM149908
149908
JM149699
149699
JM149666
149666
JM149654
149654
JM149575
149575
JM148943
148943
JM149379
149379
JM148667
148667
JM148634
148634
JM148621
148621
JM148343
148343
JM148227
148227
JM148032
148032
JM148023
148023
JM147857
147857
JM147856
147856
JM147223
147223
JM146949
146949
JM147046
147046
JM147034
147034
JM71714
71714
JM146836
146836
JM146358
146358
JM146541
146541
JM146159
146159
JM146030
146030
JM146028
146028
JM145166
145166
JM145636
145636
JM145697
145697
JM145835
145835
JM145999
145999
JM144983
144983
JM144563
144563
JM144868
144868
JM144450
144450
JM143979
143979
JM143980
143980
JM144017
144017
JM143891
143891
JM143617
143617
JM143696
143696
JM142456
142456
JM141921
141921
JM141902
141902
JM141819
141819
JM141784
141784
JM141192
141192
JM140985
140985
JM140456
140456
JM139957
139957
JM139959
139959
JM140126
140126
JM139786
139786
JM139675
139675
JM139528
139528
JM139515
139515
JM139052
139052
JM139027
139027
JM138847
138847
JM138497
138497
JM138451
138451
JM137931
137931
JM137929
137929
JM138148
138148
JM137764
137764
JM137277
137277
JM137268
137268
JM137185
137185
JM137179
137179
JM137076
137076
JM137037
137037
JM136915
136915
JM136735
136735
JM136472
136472
JM136427
136427
JM136419
136419
JM136208
136208
JM135980
135980
JM135934
135934
JM135873
135873
JM135644
135644
JM135643
135643
JM135104
135104
JM134993
134993
JM133058
133058
JM133040
133040
JM132054
132054
JM131651
131651
JM130063
130063
JM129971
129971
JM129958
129958
JM129864
129864
JM125841
125841
JM125682
125682
JM125665
125665
JM124568
124568
JM125555
125555
JM124078
124078
JM124270
124270
JM124412
124412
JM123243
123243
JM122744
122744
JM122511
122511
JM122162
122162
JM122538
122538
JM122111
122111
JM122066
122066
JM122052
122052
JM121889
121889
JM121887
121887
JM121836
121836
JM121718
121718
JM121512
121512
JM121120
121120
JM120941
120941
JM120773
120773
JM121004
121004
JM118611
118611
JM118564
118564
JM118225
118225
JM116253
116253
JM117024
117024
JM117064
117064
JM113763
113763
JM114331
114331
JM114098
114098
JM113358
113358
JM112976
112976























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































'''

# 单独下载章节
jm_photos = '''



'''


def env(name, default, trim=('[]', '""', "''")):
    import os
    value = os.getenv(name, None)
    if value is None or value == '':
        return default

    for pair in trim:
        if value.startswith(pair[0]) and value.endswith(pair[1]):
            value = value[1:-1]

    return value


def get_id_set(env_name, given):
    aid_set = set()
    for text in [
        given,
        (env(env_name, '')).replace('-', '\n'),
    ]:
        aid_set.update(str_to_set(text))

    return aid_set


def main():
    album_id_set = get_id_set('JM_ALBUM_IDS', jm_albums)
    photo_id_set = get_id_set('JM_PHOTO_IDS', jm_photos)

    helper = JmcomicUI()
    helper.album_id_list = list(album_id_set)
    helper.photo_id_list = list(photo_id_set)

    option = get_option()
    helper.run(option)
    option.call_all_plugin('after_download')


def get_option():
    # 读取 option 配置文件
    option = create_option(os.path.abspath(os.path.join(__file__, '../../assets/option/option_workflow_download.yml')))

    # 支持工作流覆盖配置文件的配置
    cover_option_config(option)

    # 把请求错误的html下载到文件，方便GitHub Actions下载查看日志
    log_before_raise()

    return option


def cover_option_config(option: JmOption):
    dir_rule = env('DIR_RULE', None)
    if dir_rule is not None:
        the_old = option.dir_rule
        the_new = DirRule(dir_rule, base_dir=the_old.base_dir)
        option.dir_rule = the_new

    impl = env('CLIENT_IMPL', None)
    if impl is not None:
        option.client.impl = impl

    suffix = env('IMAGE_SUFFIX', None)
    if suffix is not None:
        option.download.image.suffix = fix_suffix(suffix)


def log_before_raise():
    jm_download_dir = env('JM_DOWNLOAD_DIR', workspace())
    mkdir_if_not_exists(jm_download_dir)

    def decide_filepath(e):
        resp = e.context.get(ExceptionTool.CONTEXT_KEY_RESP, None)

        if resp is None:
            suffix = str(time_stamp())
        else:
            suffix = resp.url

        name = '-'.join(
            fix_windir_name(it)
            for it in [
                e.description,
                current_thread().name,
                suffix
            ]
        )

        path = f'{jm_download_dir}/【出错了】{name}.log'
        return path

    def exception_listener(e: JmcomicException):
        """
        异常监听器，实现了在 GitHub Actions 下，把请求错误的信息下载到文件，方便调试和通知使用者
        """
        # 决定要写入的文件路径
        path = decide_filepath(e)

        # 准备内容
        content = [
            str(type(e)),
            e.msg,
        ]
        for k, v in e.context.items():
            content.append(f'{k}: {v}')

        # resp.text
        resp = e.context.get(ExceptionTool.CONTEXT_KEY_RESP, None)
        if resp:
            content.append(f'响应文本: {resp.text}')

        # 写文件
        write_text(path, '\n'.join(content))

    JmModuleConfig.register_exception_listener(JmcomicException, exception_listener)


if __name__ == '__main__':
    main()
