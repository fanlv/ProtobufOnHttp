PB_PY_OUTPUT=./lark_im_pb

all: protobuf

protobuf:
	mkdir -p $(PB_PY_OUTPUT)
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/posts.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/replies.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/groups.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/entities.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/relationships.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/messages.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/chats.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/improto.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/images.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/errors.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/users.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/bots.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/chatters.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/reactions.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/reminders.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/searches.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/connections.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/contacts.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/ding.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/urgent.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/thread.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/department.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/pack.proto
	protoc -I=./idl/ --python_out=$(PB_PY_OUTPUT) ./idl/email.proto
	2to3 -nw . > /dev/null 2> /dev/null
	protoc -I=./idl/ --go_out=$$GOPATH/src ./idl/improto.proto
	protoc -I=./idl/ --go_out=$$GOPATH/src ./idl/messages.proto
	protoc -I=./idl/ --go_out=$$GOPATH/src ./idl/entities.proto
	protoc -I=./idl/ --go_out=$$GOPATH/src ./idl/frame.proto
	protoc -I=./idl/ --go_out=$$GOPATH/src ./idl/reactions.proto
	protoc -I=./idl/ --go_out=$$GOPATH/src ./idl/chats.proto
	protoc -I=./idl/ --go_out=$$GOPATH/src ./idl/errors.proto
	protoc -I=./idl/ --go_out=$$GOPATH/src ./idl/email.proto

clean:
	rm -rf $(PB_PY_OUTPUT)
