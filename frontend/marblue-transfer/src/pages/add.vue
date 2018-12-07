<script>
    export default {
        name: 'add',
        data() {
            return {
                formData: {
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
                    fromGroup: -1,
                    toGroup: -1
                }
            }
        },
        methods: {
            onSubmitBtnClicked () {

            },

            onResetBtnClicked () {

            }

        }
    }
</script>


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
                    <div class="content">
                        <Form v-model="formData" label-position="left" :label-width="100">
                            <FormItem label="QQ号">
                                <Input v-model="formData.qqNumber" />
                            </FormItem>
                            <FormItem label="现在所在的群">
                                <Select v-model="formData.fromGroup" >
                                    <Option v-for="group in formData.groupList" :value="group.value" :key="group.value">{{ group.label }}</Option>
                                </Select>
                            </FormItem>
                            <FormItem label="希望换到的群">
                                <Select v-model="formData.toGroup" >
                                    <Option v-for="group in formData.groupList" :value="group.value" :key="group.value">{{ group.label }}</Option>
                                </Select>
                            </FormItem>
                            <FormItem>
                                <Button type="primary" @click="onSubmitBtnClicked">提交</Button>
                                <Button @click="onResetBtnClicked" style="margin-left: 8px">重置</Button>
                            </FormItem>
                        </Form>
                    </div>
                </Card>
            </Content>
        </Layout>
    </div>
</template>

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

    .content {
        width: 30rem;
    }

    .content-container {
        display: flex;
        justify-content: center;
    }
</style>

