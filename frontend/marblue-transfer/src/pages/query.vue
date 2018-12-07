<template>
    <div class="layout">
        <Layout>
            <Header>
                <Menu mode="horizontal" theme="dark" active-name="1">
                    <div class="layout-nav">
                        <router-link to="/" style="color: white">三无Marblue粉丝群换群记录</router-link>
                    </div>
                </Menu>
            </Header>
            <Content>
                <Card class="content-container">
                    <Alert style="line-height: 2rem; padding: 40px 20px">
                        当前查询支持两种功能：<br>
                        1. 根据指定QQ号查询换群记录 <br>
                        2. 根据指定起止日期查询，起始日期必须早于结束日期 (查询区间左闭右开, 如要查询2018年12月7日当天，则起始日期为12月7日，结束日期为12月8日)
                    </Alert>
                    <Form ref="formCustom" :model="queryOptions" :label-width="120" style="max-width: 600px">
                        <FormItem label="QQ号">
                            <Input v-model="queryOptions.qqNumber"/>
                        </FormItem>
                        <FormItem label="起始日期">
                            <DatePicker v-model="queryOptions.startDate" type="date" placeholder="选择希望查询记录的起始日期" confirm style="width: 300px"></DatePicker>
                        </FormItem>
                        <FormItem label="结束日期">
                            <DatePicker v-model="queryOptions.endDate" type="date" placeholder="选择希望查询记录的结束日期" confirm style="width: 300px"></DatePicker>
                        </FormItem>
                        <FormItem>
                            <Button type="primary" @click="onSubmitBtnClicked">查询</Button>
                            <Button @click="onResetBtnClicked" style="margin-left: 8px">重置</Button>
                        </FormItem>
                    </Form>
                    <div class="content">
                        <Table :columns="tableColumn" :data="tableData" height="400"></Table>
                    </div>
                </Card>
            </Content>
        </Layout>
    </div>
</template>

<script>

    import { query } from "../service/api";

    export default {
        name: 'query',

        data() {
            return {
                tableColumn: [
                    {
                        title: 'QQ号',
                        key: 'qqNumber'
                    },
                    {
                        title: '原本的群',
                        key: 'fromGroup'
                    },
                    {
                        title: '换到的群',
                        key: 'toGroup'
                    },
                    {
                        title: '换群日期',
                        key: 'date'
                    }
                ],
                tableData: [],
                queryData: [
                    [
                        1,
                        '371373446',
                        2,
                        1,
                        '2018-12-02'
                    ]
                ],
                queryOptions: {
                    groupList: [
                        {
                            value: 1,
                            label: '冰工厂'
                        },
                        {
                            value: 2,
                            label: '羊毛厂'
                        },
                        {
                            value: '3',
                            label: '咖啡厂'
                        }
                    ],
                    qqNumber: '',
                    startDate: null,
                    endDate: null,
                }
            }
        },

        methods: {
            onSubmitBtnClicked() {

                const url = 'http://localhost/api/query'
                let ret
                if (this.needQueryQQNumber() && this.needQueryByDate()) {
                    ret = query(url, this.queryOptions.qqNumber,
                                    this.queryOptions.startDate.getTime(),
                                    this.queryOptions.endDate.getTime())

                } else if (this.needQueryQQNumber() && !this.needQueryByDate()) {
                    ret = query(url, this.queryOptions.qqNumber, null, null)
                } else if (!this.needQueryQQNumber() && this.needQueryByDate()) {
                    ret = query(url, null, this.queryOptions.startDate.getTime(),
                                            this.queryOptions.endDate.getTime())
                } else {
                    ret = query(url, null, null, null)
                }
                ret.then(data => {

                    this.tableData = data.data.map(record => {
                        return {
                            qqNumber: record[1],
                            fromGroup: this.getGroupName(record[2]),
                            toGroup: this.getGroupName(record[3]),
                            date: record[4]
                        }
                    })
                })
            },

            onResetBtnClicked() {
                this.queryOptions.qqNumber = ''
                this.queryOptions.startDate = null
                this.queryOptions.endDate = null
            },

            needQueryQQNumber() {
                return this.queryOptions.qqNumber != '' && /[0-9]{5,}/g.test(this.queryOptions.qqNumber)
            },
            needQueryByDate() {
                return this.queryOptions.startDate != null && this.queryOptions.endDate != null
            },

            getGroupName(groupId) {
                switch (groupId) {
                    case 1:
                        return '冰工厂'
                    case 2:
                        return '羊毛厂'
                    case 3:
                        return '咖啡厂'
                }
            }

        }
    }
</script>

<style scoped>
    .layout {
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
        height: 100%;
    }

    .layout-nav {
        margin: 0 auto;
        margin-right: 20px;
        color: white;
        font-size: 1.5rem;
    }

    .content-container {
        padding: 0 100px 100px 100px;
    }

    .query-options {
        margin: 50px 0;
    }
</style>