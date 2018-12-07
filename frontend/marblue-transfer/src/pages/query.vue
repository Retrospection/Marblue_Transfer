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
                    <Form ref="formCustom" :model="queryOptions" :label-width="120" style="max-width: 600px">
                        <FormItem label="QQ号">
                            <Input v-model="queryOptions.qqNumber"/>
                        </FormItem>
                        <FormItem label="现在所在的群">
                            <Select v-model="queryOptions.groupList">
                                <Option v-for="group in queryOptions.groupList" :value="group.value" :key="group.value">
                                    {{ group.label }}
                                </Option>
                            </Select>
                        </FormItem>
                        <FormItem label="希望换到的群">
                            <Select v-model="queryOptions.toGroup">
                                <Option v-for="group in queryOptions.groupList" :value="group.value" :key="group.value">
                                    {{ group.label }}
                                </Option>
                            </Select>
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
                        <Table :columns="tableColumn" :data="tableData"></Table>
                    </div>
                </Card>
            </Content>
        </Layout>
    </div>
</template>

<script>
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
                tableData: [
                    {
                        qqNumber: '371373446',
                        fromGroup: '羊毛厂',
                        toGroup: '冰工厂',
                        date: '2018-12-02'
                    }
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
                    fromGroup: -1,
                    toGroup: -1,

                }
            }
        },

        methods: {
            onSubmitBtnClicked() {

            },

            onResetBtnClicked() {

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