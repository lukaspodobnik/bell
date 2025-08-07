from bell.types.cmd_args.add import Date, Grade, Student


def run(
    student: Student, grade: Grade, date: Date, oral: bool, comment: str, exam: bool
):
    print(f"studen={student}, grade={grade}, date={date}, {oral=}, {comment=}, {exam=}")
