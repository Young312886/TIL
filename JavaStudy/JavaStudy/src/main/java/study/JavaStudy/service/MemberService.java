package study.JavaStudy.service;

import study.JavaStudy.domain.Member;
import study.JavaStudy.reposiotry.MemberRepository;
import study.JavaStudy.reposiotry.MemoryMemberRepository;

import java.util.List;
import java.util.Optional;

public class MemberService {
    private final MemberRepository memberRepository = new MemoryMemberRepository();

    private static void accept(Member m) throws IllegalAccessException {
        throw new IllegalAccessException("이미 존재하는 회원입니다");
    }

    //    회원 가입
    public Long join(Member member) {
        // 같은 이름의 중복 회원 거르기
//        Optional<Member> result = memberRepository.findByName(member.getName());
//        // 다만 옵셔널을 반환하는 것은 예쁘지 않다
//        result.ifPresent( m -> {
//            throw new IllegalAccessException("이미 존재하는 회원입니다")
//        });
//
        memberRepository.findByName(member.getName())
                        .ifPresent(m -> {
                            accept(m);
                        });
        memberRepository.save(member);
        return member.getId();
    }
    public List<Member> findMember() {
        return memberRepository.findall();
    }
    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }
}

