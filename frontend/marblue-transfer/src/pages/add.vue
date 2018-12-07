<script>

    import { addRecord } from '../service/api'

    export default {
        name: 'add',
        data() {
            return {
                isModalShow: false,
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
        computed: {
            fromGroupName() {
                switch (this.formData.fromGroup) {
                    case 1:
                        return '冰工厂'
                    case 2:
                        return '羊毛厂'
                    case 3:
                        return '咖啡厂'
                }
            },

            toGroupName() {
                switch (this.formData.toGroup) {
                    case 1:
                        return '冰工厂'
                    case 2:
                        return '羊毛厂'
                    case 3:
                        return '咖啡厂'
                }
            },

        },
        methods: {
            onSubmitBtnClicked () {

                const url = 'http://localhost:3535/addRecord'
                const qqNumber = this.formData.qqNumber
                const fromGroup = this.formData.fromGroup
                const toGroup = this.formData.toGroup

                if (qqNumber === '' || !(/[0-9]{5,}/g.test(qqNumber))) {
                    this.$Message.error('QQ号格式不对')
                    return
                }
                if (fromGroup === -1) {
                    this.$Message.error('应选择现在所在的群')
                    return
                }
                if (toGroup === -1) {
                    this.$Message.error('应选择希望换到的群')
                    return
                }
                if (fromGroup === toGroup) {
                    this.$Message.error('现在所在的群和希望换到的群应当不同')
                    return
                }

                const ret = addRecord(url, this.formData.qqNumber, this.formData.fromGroup, this.formData.toGroup)
                ret.then(data => {
                    if (data.code === 0) {
                        this.$Message.success(data.msg)
                    } else {
                        this.$Message.error(data.msg)
                    }
                })
            },

            onResetBtnClicked () {
                this.formData.qqNumber = ''
                this.formData.fromGroup = -1
                this.formData.toGroup = -1
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
                                <Button type="primary" @click="isModalShow = true">提交</Button>
                                <Button @click="onResetBtnClicked" style="margin-left: 8px">重置</Button>
                            </FormItem>
                        </Form>
                    </div>
                </Card>
            </Content>
            <Modal v-model="isModalShow" title="提交确认" @on-ok="onSubmitBtnClicked">
                <h1>请确认待添加的记录</h1>
                <p style="line-height: 2rem">QQ号：{{ this.formData.qqNumber }}</p>
                <p style="line-height: 2rem">现在所在的群： {{ this.fromGroupName }}</p>
                <p style="line-height: 2rem">希望换到的群： {{ this.toGroupName }}</p>
            </Modal>
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

