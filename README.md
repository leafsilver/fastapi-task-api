# FastAPI Task API

一个用于学习 FastAPI 后端工程实践的任务管理 API。

项目实现了任务的创建、查询、筛选、更新和删除，并使用 Pydantic 验证请求与响应数据。

## 功能

- 查询全部任务
- 按完成状态筛选任务
- 查询单个任务
- 创建任务
- 更新任务
- 删除任务
- 自动生成 OpenAPI 接口文档

## 环境要求

- Python 3.12 或更高版本
- uv

## 安装项目

克隆仓库：

```bash
git clone git@github.com:leafsilver/fastapi-task-api.git
cd fastapi-task-api
```

根据 `pyproject.toml` 和 `uv.lock` 创建虚拟环境并安装依赖：

```bash
uv sync
```

## 启动项目

```bash
uv run fastapi dev app/main.py
```

启动后可以访问：

- API 地址：http://127.0.0.1:8000
- Swagger 文档：http://127.0.0.1:8000/docs
- ReDoc 文档：http://127.0.0.1:8000/redoc

## API 接口

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/health` | 检查服务状态 |
| GET | `/tasks` | 查询全部任务 |
| GET | `/tasks?completed=true` | 查询已完成任务 |
| GET | `/tasks?completed=false` | 查询未完成任务 |
| GET | `/tasks/{task_id}` | 查询单个任务 |
| POST | `/tasks` | 创建任务 |
| PUT | `/tasks/{task_id}` | 完整更新任务 |
| DELETE | `/tasks/{task_id}` | 删除任务 |

## 创建任务示例

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"学习 FastAPI","completed":false}'
```

响应示例：

```json
{
  "id": 2,
  "title": "学习 FastAPI",
  "completed": false
}
```

## 项目结构

```text
fastapi-task-api/
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   └── tasks.py
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
├── .gitignore
├── README.md
├── pyproject.toml
└── uv.lock
```

- `app/main.py`：创建并组装 FastAPI 应用。
- `app/schemas.py`：定义 Pydantic 请求和响应模型。
- `app/routers/tasks.py`：定义任务相关接口。
- `pyproject.toml`：记录项目元数据和直接依赖。
- `uv.lock`：锁定完整依赖版本。

## 当前限制

任务暂时保存在 Python 进程的内存中。修改代码或重启服务器后，任务数据会恢复为初始状态。

后续可以接入数据库实现持久化存储。